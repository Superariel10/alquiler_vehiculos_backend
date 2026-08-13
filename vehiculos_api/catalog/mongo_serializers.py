from rest_framework import serializers

class Fleet_logsSerializer(serializers.Serializer):
    _id = serializers.IntegerField()
    id_vehiculo = serializers.IntegerField()
    class Action:
        CREATED = "created"
        UPDATED = "updated"
        MAINTENANCE  = "maintenance"
        DISABLED = "disabled"
    
        CHOICES = [
            (CREATED, "Created"),
            (UPDATED, "Updated"),
            (MAINTENANCE, "Maintenance"),
            (DISABLED, "Disabled"),
        ]

    action = serializers.ChoiceField(
        choices=Action.CHOICES,
        default=Action.DISABLED
    )
    note = serializers.CharField(max_length=120)
    class Source:
        SYSTEM = "system"
        MOBILE = "mobile"
        
        CHOICES = [
            (SYSTEM, "System"),
            (MOBILE, "Mobile"),
        ]
    source = serializers.ChoiceField(
        choices=Source.CHOICES,
        default=Source.SYSTEM
    )
    created_at = serializers.DateTimeField(required=False)

class Rental_eventsSerializer(serializers.Serializer):
    _id = serializers.IntegerField()        
    rental_id = serializers.CharField()      
    class Event_Type:
            CREATED = "created"
            PICKED_UP = "picked_up"
            RETURNED  = "returned"
            PAID = "paid"
            CANCELLED = "cancelled"
        
            CHOICES = [
                (CREATED, "Created"),
                (PICKED_UP, "Picked Up"),
                (RETURNED, "Returned"),
                (PAID, "Paid"),
                (CANCELLED, "Cancelled"),
            ]
    event_type = serializers.ChoiceField(
        choices=Event_Type.CHOICES,
        default=Event_Type.CREATED
    )  
    class Source:
        SYSTEM = "system"
        MOBILE = "mobile"
        WEB = "web"
            
        CHOICES = [
            (SYSTEM, "System"),
            (MOBILE, "Mobile"),
            (WEB, "Web"),
        ]
    source = serializers.ChoiceField(
        choices=Source.CHOICES,
        default=Source.SYSTEM
    ) 
    note = serializers.CharField(required=False, allow_blank=True)
    created_at = serializers.DateTimeField(required=False)
