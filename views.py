from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def bfhl(request):
    if request.method == 'POST':
        try:
            # Ensure that 'data' key exists and is a list
            data = request.data.get('data', [])
            if not isinstance(data, list):
                return Response({"is_success": False, "error": "Invalid data format, 'data' should be a list."}, status=400)

            # Process numbers and alphabets
            numbers = [x for x in data if x.isdigit()]
            alphabets = [x for x in data if x.isalpha()]
            highest_alphabet = max(alphabets, default='', key=lambda x: x.upper())

            response = {
                "is_success": True,
                "user_id": "your_fullname_dob",
                "email": "your_email@example.com",
                "roll_number": "your_roll_number",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": [highest_alphabet] if highest_alphabet else []
            }
        except Exception as e:
            response = {"is_success": False, "error": str(e)}
        return Response(response)

    return Response({"operation_code": 1})
