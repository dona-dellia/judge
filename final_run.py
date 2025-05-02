import jira_issue_extractor as jix
import test_scenario_enriched as tse
import test_case_generator as tcg
import test_case_executor as tce

if __name__ == "__main__":
    
    ID_PROJECT = "A123"
    user_stories = jix.get_all_use_stories(ID_PROJECT)
    need_enrichment = False
    need_human = []
    
    for user_story in user_stories:
        test_scenarios = jix.get_all_test_scenarios(user_story)

        for test_scenario in test_scenarios:                    
                test_cases = tcg.generate_test_cases(test_scenario)
                report = tce.execute(test_cases)
                
                if(report.success):
                    status = jix.upload(report)
                    if status:
                        print("Fluxo básico OK!")

                elif(report.fail and ~test_cases.enriched):
                     enrich_us = tse.enrich_use_story(user_story)
                     new_test_cases = tcg.generate_test_cases(enrich_us)
                     jix.inform_human(new_test_cases)

                else:
                    need_human.append(user_story)

    for informs in need_human:
         jix.inform_human(informs)

