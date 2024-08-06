import httpx
import asyncio

BASE_URL = "http://127.0.0.1:8000" 

async def test_users():
    async with httpx.AsyncClient() as client:
        # Test GET /users
        response = await client.get(f"{BASE_URL}/users/")
        print("GET /users")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test POST /users
        payload = {"name": "John Doe", "email": "john@example.com"}
        response = await client.post(f"{BASE_URL}/users/", json=payload)
        print("POST /users")
        print("Status code:", response.status_code)
        
        try:
            response_data = response.json()
            print("Response:", response_data)
            user_id = response_data.get("id")
        except httpx.HTTPStatusError as e:
            print("Error while making request:", e)
            print("Response content:", response.text)
            return
        except ValueError as e:
            print("Error decoding JSON:", e)
            print("Response content:", response.text)
            return

        # Test GET /users/{user_id}
        response = await client.get(f"{BASE_URL}/users/{user_id}")
        print("GET /users/{user_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test PATCH /users/{user_id}
        update_payload = {"name": "John Updated"}
        response = await client.patch(f"{BASE_URL}/users/{user_id}", json=update_payload)
        print("PATCH /users/{user_id}")
        print("Status code:", response.status_code)
        print("Response content:", response.text) 
        
        try:
            print("Response:", response.json())
        except ValueError as e:
            print("Error decoding JSON:", e)
            print("Response content:", response.text)

        # Test DELETE /users/{user_id}
        response = await client.delete(f"{BASE_URL}/users/{user_id}")
        print("DELETE /users/{user_id}")
        print("Status code:", response.status_code)

async def test_accommodations():
    async with httpx.AsyncClient() as client:
        # Test GET /accommodations
        response = await client.get(f"{BASE_URL}/accommodations/")
        print("GET /accommodations")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test POST /accommodations
        payload = {
                    "name": "aaa",
                    "location": "string",
                    "price": 10000,
                    "start_date": "2024-08-06T01:16:29.110Z",
                    "end_date": "2024-08-06T01:16:29.110Z",
                    "city_id": 1,
                    "travel_id": 1
                }  
        response = await client.post(f"{BASE_URL}/accommodations/", json=payload)
        print("POST /accommodations")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        accommodation_id = response.json().get("id")

        # Test GET /accommodations/{accommodation_id}
        response = await client.get(f"{BASE_URL}/accommodations/{accommodation_id}")
        print("GET /accommodations/{accommodation_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test PATCH /accommodations/{accommodation_id}
        update_payload = {"name": "Hotel"} 
        response = await client.patch(f"{BASE_URL}/accommodations/{accommodation_id}", json=update_payload)
        print("PATCH /accommodations/{accommodation_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test DELETE /accommodations/{accommodation_id}
        response = await client.delete(f"{BASE_URL}/accommodations/{accommodation_id}")
        print("DELETE /accommodations/{accommodation_id}")
        print("Status code:", response.status_code)


async def test_transport():
    async with httpx.AsyncClient() as client:
        # Test GET /transports
        response = await client.get(f"{BASE_URL}/transports/")
        print("GET /transports")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test POST /transports
        payload = {
            "type": "Bus",
            "company": "Transportes ABC",
            "price": 150.0,
            "start_datetime": "2024-08-06T08:00:00",
            "start_location": "AAA ",
            "end_datetime": "2024-08-06T12:00:00",
            "end_location": "BBB",
            "start_city_id": 1,  
            "end_city_id": 2,    
            "travel_id": 1       
        }
        response = await client.post(f"{BASE_URL}/transports/", json=payload)
        print("POST /transports")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        transport_id = response.json().get("id") 

        # Test GET /transports/{transport_id}
        response = await client.get(f"{BASE_URL}/transports/{transport_id}")
        print(f"GET /transports/{transport_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test PATCH /transports/{transport_id}
        update_payload = {
            "company": "Transportes XYZ",  
            "price": 1750000             
        }
        response = await client.patch(f"{BASE_URL}/transports/{transport_id}", json=update_payload)
        print(f"PATCH /transports/{transport_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test DELETE /transports/{transport_id}
        response = await client.delete(f"{BASE_URL}/transports/{transport_id}")
        print(f"DELETE /transports/{transport_id}")
        print("Status code:", response.status_code)


async def test_activity():
    async with httpx.AsyncClient() as client:
        # Test GET /activities
        response = await client.get(f"{BASE_URL}/activities/")
        print("GET /activities")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test POST /activities
        payload = {
            "name": "City Tour",
            "description": "A tour through the city",
            "location": "Downtown",
            "start_datetime": "2024-08-06T14:00:00",
            "price": 30.0,
            "duration": 120,
            "city_id": 1, 
            "travel_id": 1
        }

        response = await client.post(f"{BASE_URL}/activities/", json=payload)
        print("POST /activities")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        activity_id = response.json().get("id") 

        # Test GET /activities/{activity_id}
        response = await client.get(f"{BASE_URL}/activities/{activity_id}")
        print(f"GET /activities/{activity_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test PATCH /activities/{activity_id}
        update_payload = {
            "name": "City Tour Updated",
            "description": "An updated guided tour through the city"
        }
        response = await client.patch(f"{BASE_URL}/activities/{activity_id}", json=update_payload)
        print(f"PATCH /activities/{activity_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test DELETE /activities/{activity_id}
        response = await client.delete(f"{BASE_URL}/activities/{activity_id}")
        print(f"DELETE /activities/{activity_id}")
        print("Status code:", response.status_code)


async def test_expense():
    async with httpx.AsyncClient() as client:
        # Test POST /expenses
        payload = {
            "description": "Lunch with colleagues",
            "amount": 45.75,
            "datetime": "2024-08-06T12:00:00",
            "user_id": 1,
            "travel_id": 2
        }
        response = await client.post(f"{BASE_URL}/expenses/", json=payload)
        print("POST /expenses")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        expense_id = response.json().get("id")  

        # Test GET /expenses/{expense_id}
        response = await client.get(f"{BASE_URL}/expenses/{expense_id}")
        print("GET /expenses/{expense_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test PATCH /expenses/{expense_id}
        update_payload = {"description": "Lunch Updated"} 
        response = await client.patch(f"{BASE_URL}/expenses/{expense_id}", json=update_payload)
        print("PATCH /expenses/{expense_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test DELETE /expenses/{expense_id}
        response = await client.delete(f"{BASE_URL}/expenses/{expense_id}")
        print("DELETE /expenses/{expense_id}")
        print("Status code:", response.status_code)

async def test_city():
    async with httpx.AsyncClient() as client:
        # Test GET /cities
        response = await client.get(f"{BASE_URL}/cities/")
        print("GET /cities")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test POST /cities
        payload = {"name": "Paris", "country": "France"}  
        response = await client.post(f"{BASE_URL}/cities/", json=payload)
        print("POST /cities")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        city_id = response.json().get("id")  

        # Test PATCH /cities/{city_id}
        update_payload = {"name": "Paris Updated"} 
        response = await client.patch(f"{BASE_URL}/cities/{city_id}", json=update_payload)
        print("PATCH /cities/{city_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test DELETE /cities/{city_id}
        response = await client.delete(f"{BASE_URL}/cities/{city_id}")
        print("DELETE /cities/{city_id}")
        print("Status code:", response.status_code)

async def test_travel():
    async with httpx.AsyncClient() as client:
        # Test POST /travels
        payload = {
            "name": "Trip to Paris",
            "start_date": "2024-08-06T12:00:00",
            "end_date": "2024-08-07T12:00:00"
            }

        response = await client.post(f"{BASE_URL}/travels/", json=payload)
        print("POST /travels")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        travel_id = response.json().get("id") 

        # Test GET /travels/{travel_id}
        response = await client.get(f"{BASE_URL}/travels/{travel_id}")
        print("GET /travels/{travel_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test PATCH /travels/{travel_id}
        update_payload = {"name": "Trip to Paris Updated"}
        response = await client.patch(f"{BASE_URL}/travels/{travel_id}", json=update_payload)
        print("PATCH /travels/{travel_id}")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test DELETE /travels/{travel_id}
        response = await client.delete(f"{BASE_URL}/travels/{travel_id}")
        print("DELETE /travels/{travel_id}")
        print("Status code:", response.status_code)

        # Test GET /travels/{travel_id}/users
        response = await client.get(f"{BASE_URL}/travels/{travel_id}/users")
        print("GET /travels/{travel_id}/users")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test POST /travels/{travel_id}/users
        user_payload = {"user_id": 1} 
        response = await client.post(f"{BASE_URL}/travels/{travel_id}/users", json=user_payload)
        print("POST /travels/{travel_id}/users")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test DELETE /travels/{travel_id}/users/{user_id}
        response = await client.delete(f"{BASE_URL}/travels/{travel_id}/users/1")
        print("DELETE /travels/{travel_id}/users/{user_id}")
        print("Status code:", response.status_code)

        # Test GET /travels/{travel_id}/accommodations
        response = await client.get(f"{BASE_URL}/travels/{travel_id}/accommodations")
        print("GET /travels/{travel_id}/accommodations")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test GET /travels/{travel_id}/transports
        response = await client.get(f"{BASE_URL}/travels/{travel_id}/transports")
        print("GET /travels/{travel_id}/transports")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test GET /travels/{travel_id}/activities
        response = await client.get(f"{BASE_URL}/travels/{travel_id}/activities")
        print("GET /travels/{travel_id}/activities")
        print("Status code:", response.status_code)
        print("Response:", response.json())

        # Test GET /travels/{travel_id}/expenses
        response = await client.get(f"{BASE_URL}/travels/{travel_id}/expenses")
        print("GET /travels/{travel_id}/expenses")
        print("Status code:", response.status_code)
        print("Response:", response.json())

async def run_tests():
    #await test_users()
    #await test_accommodations()
    #await test_transport()
    #await test_activity()
    #await test_expense()
    
    #await test_city()
    await test_travel()

if __name__ == "__main__":
    asyncio.run(run_tests())
