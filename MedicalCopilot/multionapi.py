from multion.client import MultiOn
import agentops

client = MultiOn(
    api_key="6e5f65dc1d7e4254a45ee1028ca4f64b",
    agentops_api_key="ded98bd6-89f0-4dcf-8583-65ba49226cc5",
)

agentops.init(auto_start_session=False, tags=["Amina"])

response = client.browse(
    cmd="Fill out a form.name: Jane Smith, status: Active, date: 2024-07-20, publisher: XYZ Health Services, description: This form is intended to document the mental health support plan for an individual experiencing depression., purpose: The purpose of this form is to outline the treatment and support strategies for managing the patient's depression., general_information: The general information provided in this form will assist healthcare professionals in developing an effective treatment plan for the patient suffering from depression., current_date: 2024-07-20",
    url="https://app.medplum.com/Questionnaire/new",
    local=True,
    agent_id="0414969a",
    # agent_id = 
)
# documentation if needed
# session_id = response.session_id

# response = client.browse(
#     cmd="give me the information",
#     local=True,
#     agent_id="0414969a",
#     session_id=session_id
#     # agent_id = 
# )
