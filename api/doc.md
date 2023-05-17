# FastAPI
## Version: 0.1.0

### /login

#### GET
##### Summary:

Login

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| log | query |  | Yes |  |
| password | query |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | ID of user |
| 404 | User not found |
| 422 | Validation Error |

### /register

#### GET
##### Summary:

Register

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| log | query |  | Yes |  |
| password | query |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | ID of user |
| 405 | User already exists |
| 422 | Validation Error |

### /

#### GET
##### Summary:

Main

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |

### /find

#### GET
##### Summary:

Find

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| line | query |  | Yes |  |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | list of products |
| 404 | Product not found |
| 422 | Validation Error |

### /rate

#### POST
##### Summary:

Rate

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| prod_id | query |  | Yes | integer |
| user_rate | query |  | Yes | boolean |
| user_id | cookie |  | No | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 202 | Accepted |
| 404 | Need to login |
| 422 | Validation Error |

### /get recommendations

#### GET
##### Summary:

Get Recommendations

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | cookie |  | No | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 202 | Accepted |
| 404 | Need to login |
| 422 | Validation Error |
