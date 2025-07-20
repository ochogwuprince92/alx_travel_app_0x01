from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Seed the database with listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()

        for i in range(5):
            listing = Listing.objects.create(
                title=f"Hotel {i}",
                location=f"City {i}",
                price=random.uniform(100, 500),
                description="Great place to stay!"
            )

            for j in range(2):
                Booking.objects.create(
                    listing=listing,
                    customer_name=f"Customer {j}",
                    booking_date=date.today() + timedelta(days=j)
                )

                Review.objects.create(
                    listing=listing,
                    reviewer_name=f"Reviewer {j}",
                    rating=random.randint(1, 5),
                    comment="Nice experience!"
                )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully."))
