# This script do for you the commands to copy, delete and move files or directories to the path you tell it to do.

# Import some module of python
import os
import shutil

def main():
    while True:
        try:
            start_command = input('''
            1. Copy
            2. Delete
            3. Move
            4. Exit
            Choose one number:
            ''')
        except:
            print('Error! Please check the path!')
        if start_command == '1':
            copy()
        elif start_command == '2':
            delete()
        elif start_command == '3':
            move()
        elif start_command == '4':
            print('See you soon!')
            break

def copy():
    try:
        copy_action = input('''
        1. Copy all the directory
        2. Copy only one files
        3. Copy two or more files
        Choose one number:
        ''')
    except:
        print('Something has failed!')
    if copy_action == '1':
        copy_path_source = input('What path do you want to copy?: ')
        copy_path_destination = input('Where do you copy the directory?: ')
        shutil.copy(copy_path_source, copy_path_destination)

def delete():
    try:
        delete_action = input('''
        1. Delete all the directory
        2. Delete only one files
        3. Delete two or more files
        Choose one number:
        ''')
    except:
        print('Something has failed!')
    if delete_action == '1':
        delete_path_source = input('What path do you want to copy?: ')
        shutil.delete(delete_path_source)

def move():
    try:
        move_action = input('''
        1. Move all the directory
        2. Move only one files
        3. Move two or more files
        Choose one number:
        ''')
    except:
        print('Something has failed!')
    if move_action == '1':
        move_path_source = input('What path do you want to copy?: ')
        move_path_destination = input('Where do you copy the directory?: ')
        shutil.move(move_path_source, move_path_destination)