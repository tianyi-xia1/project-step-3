#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from memorization.classes import Status

class StatusManager:
    def __init__(self):
        self.correct_first_time = set()
        self.failed_first_time = set()

    def update_status(self, word_pair, result):
        try:
            if not hasattr(word_pair, 'status'):
                raise AttributeError("word_pair object must have a 'status' attribute.")
            
            if result not in ['correct', 'incorrect']:
                raise ValueError("Result must be either 'correct' or 'incorrect'.")

            if word_pair.status is None:
                if result == 'correct':
                    self.correct_first_time.add(word_pair)
                    word_pair.status = Status.CORRECT_FIRST_TIME
                elif result == 'incorrect':
                    self.failed_first_time.add(word_pair)
                    word_pair.status = Status.FAILED_FIRST_TIME
        except AttributeError as ex:
            print(f"Attribute Error: {ex}")
        except ValueError as ex:
            print(f"Value Error: {ex}")
        except TypeError as ex:
            print(f"Type Error: {ex}")
        except Exception as ex:
            print(f"Unexpected Error: {ex}")


def view_progress(status_manager):
    try:
        if not isinstance(status_manager, StatusManager):
            raise TypeError("status_manager must be an instance of StatusManager.")

        print("\nWords correctly answered on the first attempt:")
        if status_manager.correct_first_time:
            for pair in status_manager.correct_first_time:
                print(f"{pair.french} - {pair.english}")
        else:
            print("None")

        print("\nWords failed on the first attempt:")
        if status_manager.failed_first_time:
            for pair in status_manager.failed_first_time:
                print(f"{pair.french} - {pair.english}")
        else:
            print("None")
    except TypeError as ex:
        print(f"Type Error: {ex}")
    except Exception as ex:
        print(f"Unexpected Error: {ex}")


