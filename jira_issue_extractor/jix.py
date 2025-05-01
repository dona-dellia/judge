
import json

def get_all_use_stories(id):
    """
    """
    json = """
            {
                "id": "10051",
                "key": "TESTGEN-52",
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

def upload(report):
    """
    """
    try:
        json.loads(report)
        return True
    except ValueError:
        return False
