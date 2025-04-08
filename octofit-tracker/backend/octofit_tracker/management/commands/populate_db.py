from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=30),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        User.objects.bulk_create(users)

        # Convert ObjectId to string for id fields
        for user in users:
            user.id = str(ObjectId())
            user.save()

        # Create teams
        teams = [
            Team(name='Blue Team'),
            Team(name='Gold Team')
        ]
        Team.objects.bulk_create(teams)

        # Convert ObjectId to string for id fields
        for team in teams:
            team.id = str(ObjectId())
            team.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60),
            Activity(user=users[1], type='Crossfit', duration=120),
            Activity(user=users[2], type='Running', duration=90),
            Activity(user=users[3], type='Strength', duration=30),
            Activity(user=users[4], type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Convert ObjectId to string for id fields
        for activity in activities:
            activity.id = str(ObjectId())
            activity.save()

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=teams[0], score=100),
            Leaderboard(team=teams[1], score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Convert ObjectId to string for id fields
        for entry in leaderboard_entries:
            entry.id = str(ObjectId())
            entry.save()

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        # Convert ObjectId to string for id fields
        for workout in workouts:
            workout.id = str(ObjectId())
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))