import os
import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Automatically format Python code and organize imports in the Django project"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            default=".",
            help="Path to the Django project (default: current directory)",
        )

    def handle(self, *args, **options):
        path = options["path"]
        self.stdout.write(f"Formatting code in: {path}")

        try:
            # Run isort to organize imports
            subprocess.run(["isort", path], check=True)
            self.stdout.write(self.style.SUCCESS("Imports organized successfully."))

            # Run Black to format the code
            subprocess.run(["black", path], check=True)
            self.stdout.write(self.style.SUCCESS("Code formatted successfully."))
        except subprocess.CalledProcessError as e:
            self.stderr.write(f"Error during formatting: {e}")
