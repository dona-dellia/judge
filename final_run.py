import jira_interactor as jix
import test_scenario_enriched as tse
import test_case_generator as tcg
import test_case_executor as tce

if __name__ == "__main__":
    
    JIRA_BOARD_ID = "4217911"
    THRESHOLD = .7
    user_stories = jix.get_all_use_stories(JIRA_BOARD_ID)
    #especificar os lista de ids de interesse
    # issues_keys
    need_human = []
    list_ids_processed = []
    
    for user_story in user_stories:
        us_id = user_story['id']
        test_scenarios = jix.get_all_test_scenarios(user_story.id)

        for test_scenario in test_scenarios:                    
                test_cases = tcg.generate_test_cases(test_scenario)
                report = tce.execute(test_cases)
                
                if(report['result'] < THRESHOLD):
                    status = jix.upload(report)
                    if status:
                        print("Fluxo básico OK!")

                elif(report['result'] > THRESHOLD and (us_id not in list_ids_processed)):
                    list_ids_processed.append(us_id)
                    enrich_us = tse.enrich_use_story(user_story, report.feedback)
                    jix.inform_human(enrich_us)
                else:
                    need_human.append(user_story)

    for informs in need_human:
        jix.inform_human(informs)

