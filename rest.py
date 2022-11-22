import requests

ACCESS_TOKEN = None
INST_URI = None
PARAMS = {
    "grant_type": "password",
    "client_id": "3MVG9I9urWjeUW051PumYX1mbS5HkS3kpZsbCEzYWjgivRyDno1MjvM08EfVf2be52s0vrthHamsgMpQCrm5Z",
    "client_secret": "EC97DAFBF9F6F2399DE5E7BADA2E9BBEF6B3B6E832DC435668AA452940AD9501",
    "username": "soljit_algeria2@soljit.com",
    "password": "entretient_1235zoLmTaUDLiouUaOAN6WhOQPi"
}
URL = "https://login.salesforce.com/services/oauth2/token"
HEADERS = {
    "Content-Type": "application/json",
}


def get_access(params):
    global ACCESS_TOKEN
    global INST_URI
    global HEADERS

    response = requests.post(URL, params=PARAMS)
    INST_URI = response.json().get('instance_url', "")
    ACCESS_TOKEN = response.json().get('access_token', "")
    print('*********connecting to api*********')
    print('access token : ' + ACCESS_TOKEN)
    print('instance url : ' + INST_URI)
    HEADERS['Authorization'] = "Bearer {0}".format(ACCESS_TOKEN)


def get_candidature(candid_id, field="First_Name__c,Last_Name__c,Year__c,Year_Of_Experience__c"):
    print(f"*********get candidature with id {candid_id} **********")
    response = requests.get(INST_URI + f"/services/data/v55.0/sobjects/Candidature__c/{candid_id}?fields={field}"
                            , headers=HEADERS)
    keys = field.split(',')
    for k in keys:
        print(k + "  :  " + str(response.json().get(k)))


def create_candidature(first_name, last_name, year_of_xp):
    url = INST_URI + "/services/data/v55.0/sobjects/Candidature__c/"
    body = {
        "First_Name__c": first_name,
        "Last_Name__c": last_name,
        "Year_Of_Experience__c": year_of_xp
    }
    response = requests.post(url,json=body,headers=HEADERS)
    if response.json().get('success', False):
        print('candidature has been added successfuly')
    else:
        print('Error while creating new candidature')


def update_candidature(candid_id, body):
    url = INST_URI + f"/services/data/v55.0/sobjects/Candidature__c/{candid_id}"
    response = requests.patch(url, json=body, headers=HEADERS)
    if response.status_code == 204:
        print('candidature updated successfuly')
    else:
        print(f'Error while updating candidature{candid_id}')


def get_all_candidatures():
    url = INST_URI + "/services/data/v55.0/query/?q=SELECT id,First_Name__c,Last_Name__c,Year_of_experience__c from Candidature__c"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()['records']
    print('error while retrieving all candidatures')
    return None


def search_candidate(criterion, value):
    url = INST_URI + f"/services/data/v55.0/query/?q=SELECT id from Candidature__c where {criterion}={value}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()['records']
    print('error while searching for candidates, msg:'+str(response.json()))
    return None


def group_candidature():
    url = INST_URI + f"/services/data/v55.0/query/?q=SELECT count(id),type__c from Candidature__c group by type__c"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()['records']
    print('error while searching for candidates, msg:' + str(response.json()))
    return None


if __name__ == "__main__":
    get_access(PARAMS)
    #get_candidature("a004L000002gCJK")
    #create_candidature("khaoula","saadi",1.0)
    body = {
        "Last_Name__c": "'saadi'"
    }
    #update_candidature("a004L000002gCJK", body)
    #get_all_candidatures()
    #print(search_candidate('Year_of_experience__c', 1.0))
    print(group_candidature())
