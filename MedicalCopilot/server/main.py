from typing import Union
from multion.client import MultiOn

import boto3
from fastapi import FastAPI
from pydantic import BaseModel




class Payload(BaseModel):
    text: str

# Initialize the AWS Comprehend Medical client
session = boto3.Session(profile_name='Dev')
comprehend_medical = session.client(service_name='comprehendmedical', region_name='us-east-1')


app = FastAPI()

def get_icd10_codes_and_symptoms(text):
    try:
        # Call the detect_entities_v2 API
        result = comprehend_medical.infer_icd10_cm(Text=text)

        # Extract the ICD-10-CM codes and symptoms from the response
        icd10_codes = []
        symptoms = []

        for entity in result['Entities']:
            # Extract ICD-10-CM codes if available
            if 'ICD10CMConcepts' in entity and entity['ICD10CMConcepts']:
                for concept in entity['ICD10CMConcepts']:
                    icd10_codes.append({
                        'Code': concept['Code'],
                        'Description': concept['Description'],
                        'Score': concept['Score']
                    })
            # Extract symptoms if the entity is categorized as a symptom
            if 'Traits' in entity:
                for trait in entity['Traits']:
                    if trait['Name'] == 'SYMPTOM':
                        symptoms.append({
                            'Symptom': entity['Text'],
                            'Score': trait['Score']
                        })

        return {
            'ICD10Codes': icd10_codes,
            'Symptoms': symptoms
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'ICD10Codes': [],
            'Symptoms': []
        }



@app.post("/text-chunk")
def text_chunk(payload: Payload):
    print("received text: ", payload.text)
    result = get_icd10_codes_and_symptoms(payload.text)
    print("result: ", result)

    for code in result['ICD10Codes']:
        if code['Code'] == 'Z72.820':

            client = MultiOn(
                api_key="8c89f945ade14a7e95a59f7f935b8c2b",
            )

            response = client.browse(
                cmd = "Wait 2 seconds. Log in. Submit email 'salwansandeep5@gmail.com' and password 'Medreport!'",
                url="https://app.medplum.com/Questionnaire/new",
                local=True,
            )


            """
            response = client.browse(
                cmd = "Wait 2 seconds. Log in. Submit email 'salwansandeep5@gmail.com' and password 'Medreport!'",
                url="https://app.medplum.com/Questionnaire/new",
                local=True,
            )
            """
            print("The patient is experiencing sleep deprivation.")

    return result



@app.get("/test")
def test():
    client = MultiOn(
        api_key="8c89f945ade14a7e95a59f7f935b8c2b",
    )

    response = client.browse(
        cmd = "Wait 2 seconds. Log in. Submit email 'salwansandeep5@gmail.com' and password 'Medreport!'",
        url="https://app.medplum.com/Questionnaire/new",
        local=True,
    )

    """

    client = MultiOn(
        api_key="6e5f65dc1d7e4254a45ee1028ca4f64b",
    )
    response = client.browse(
        cmd="Fill out a form.name: Jane Smith, status: Active, date: 2024-07-20, publisher: XYZ Health Services, description: This form is intended to document the mental health support plan for an individual experiencing depression., purpose: The purpose of this form is to outline the treatment and support strategies for managing the patient's depression., general_information: The general information provided in this form will assist healthcare professionals in developing an effective treatment plan for the patient suffering from depression., current_date: 2024-07-20",
        url="https://app.medplum.com/Questionnaire/new",
        local=True,
        agent_id="0414969a",
    )
    """

    return {"response": "success"}