from django.shortcuts import render

def contacts_view(request):
    data = {
        "title": "Contacts page",
        "name": "Contacts",
        "contacts": {
            "Address": "22 Satbaev str., 050013, Almaty, the Republic of Kazakhstan",
            "Phone number": "+7 (727) 292 60 25",
            "Email": "info@satbayev.university",
        },
        "features": [
            "Open 24/7",
            "Friendly support",
            "Located in the city center",
        ]
    }
    return render(request, 'contacts.html', data)