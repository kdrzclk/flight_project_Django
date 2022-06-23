from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Flight, Passenger, Reservation



class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )