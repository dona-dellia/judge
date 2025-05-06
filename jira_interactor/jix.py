
import json
# - User Story: tem summary

# - Test Scenario: Sumário + GIVEN WHEN THEN
# - KEY: "TESTGEN-52" 


def get_all_use_stories(id):
    """
    """
    json = """
            {
                "id": "10051",
                "key": "TESTGEN-52",
                "enriched":1
                "fields": 
                    {
                        "summary": "Documentação",
                        "status": 
                        {
                            "description": "ACCEPTANCE CRITERIA GOES HERE",
                            "name": "In Progress"
                        }
                }
            }
            """
    return json

def get_all_test_scenarios(user_story_id):
    json = """
                {
                    "ID": "4217911",
                    "Key": "CMBM-8290",
                    "Summary": "Production Support",
                    "Description": "As a Prism CM adapter team, we want to support any issues that pops up form the production",
                    "Status": "In Development",
                    "Priority": "P4 - Medium",
                    "Assignee": "Arindam_Biswas1",
                    "AssigneeEmail": "Arindam_Biswas1@Dell.com",
                    "Reporter": "Jennefer_J",
                    "ReporterEmail": "Jennefer_J@Dell.com",
                    "AcceptanceCriteria": "GIVEN the cm adapter application\r\n\r\nWHEN there is a production issue\r\n\r\nTHEN as a team we will make sure the issue is addressed on time \r\n\r\n ",
                    "E2E": "No"
                }
            """
    json.dump(json)
    return json

def upload(report):
    """
    """
    try:
        json.loads(report)
        return True
    except ValueError:
        return False
