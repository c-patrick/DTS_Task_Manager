# Task Management API Documentation

## Get Task Details (JSON)

Retrieve detailed information about a specific task by its ID in JSON format.

---

### Endpoint

`GET /api/task/{task_id}`

---

### Path Parameters

| Parameter | Type    | Description          | Required |
| --------- | ------- | -------------------- | -------- |
| task_id   | integer | The unique ID of the task to retrieve | Yes      |

---

### Response

- **200 OK**: Returns the JSON representation of the task.
- **404 Not Found**: Task with the specified ID does not exist.

---

### Response Body (200)

```json
{
  "id": 123,
  "title": "Task Title",
  "description": "Detailed description of the task",
  "due_date": "2025-05-20",
  "priority": "High",
  "user_id": 5,
  "username": "johndoe"
}
```

| Field         | Type                  | Description                                      |
| ------------- | --------------------- | ------------------------------------------------ |
| `id`          | integer               | Task unique identifier                           |
| `title`       | string                | Title of the task                                |
| `description` | string or null        | Detailed description (nullable)                  |
| `due_date`    | string (date) or null | Due date in ISO format (nullable)                |
| `priority`    | string or null        | Priority level ("Low", "Medium", "High") or null |
| `user_id`     | integer               | ID of the assigned user                          |
| `username`    | string                | Username of the assigned user                    |

---

### Example Request
```http
GET /api/task/123 HTTP/1.1
Host: localhost:5000
Accept: application/json
```
---

### Example Response
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 123,
  "title": "Finish report",
  "description": "Complete the quarterly financial report",
  "due_date": "2025-05-20",
  "priority": "High",
  "user_id": 5,
  "username": "johndoe"
}
```
---

### Errors
* **404 Not Found**
```json
{
  "message": "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
}
```