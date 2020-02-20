#!/usr/bin/python3
"""
Contains the Storage
"""
from models.engine.file_storage import FileStorage
from models import base_model

storage = FileStorage()
storage.reload()

