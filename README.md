# Admin

### Documentation for all Functions

1. **ADD(payments: dict, nr: int, val: dict, changes: list)**
   - Description: The `ADD` function updates a payment dictionary and records the type of operation ('MOD' or 'ADD').
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `nr` (int): The number of the apartment to be modified.
     - `val` (dict): The value to be introduced or modified.
     - `changes` (list): A list where changes are recorded.
   - Returns: Nothing

2. **DEL(payments: dict, nr: int, changes: list)**
   - Description: The `DEL` function deletes a payment dictionary and records the type of operation.
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `nr` (int): The number of the apartment to be modified.
     - `changes` (list): A list where changes are recorded.
   - Returns: Nothing

3. **mass_DEL(payments: dict, start: int, end: int, changes: list)**
   - Description: The `mass_DEL` function deletes payments between the indexes `start` and `end` and records the type of operation.
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `start` (int): The starting index of apartments to be deleted.
     - `end` (int): The ending index of apartments to be deleted.
     - `changes` (list): A list where changes are recorded.
   - Returns: Nothing

4. **mass_UNDO(payments: dict, changes: list, rec: int)**
   - Description: The `mass_UNDO` function iteratively undoes changes in a payment dictionary based on a specified number of records (`rec`).
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `rec` (int): The number of undos to be made.
     - `changes` (list): A list where changes are recorded.
   - Returns: Nothing

5. **inDEL(payments: dict, nr: int)**
   - Description: The `inDEL` function deletes a payment dictionary.
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `nr` (int): The number of the apartment to be modified.
   - Returns: Nothing

6. **inADD(payments: dict, nr: int, val: dict)**
   - Description: The `inADD` function updates a payment dictionary.
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `nr` (int): The number of the apartment to be modified.
     - `val` (dict): The value to be introduced or modified.
   - Returns: Nothing

7. **UNDO(payments: dict, changes: list)**
   - Description: The `UNDO` function reverses the most recent payment operation recorded in the `changes` list and updates the `payments` dictionary accordingly.
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `changes` (list): A list where changes are recorded.
   - Returns: Nothing

8. **mass_MOD(payments: dict, start: int, end: int, key: str, value: float, changes: list)**
   - Description: The `mass_MOD` function iteratively modifies payment information within a specified range and records a 'mMOD' operation in the `changes` list to indicate the mass modification.
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `start` (int): The starting index of apartments to be modified.
     - `end` (int): The ending index of apartments to be modified.
     - `key` (str): The key to be modified.
     - `value` (float): The new value of the key to be modified.
     - `changes` (list): A list where changes are recorded.
   - Returns: Nothing

9. **get_gas_value(nr, payments)**
   - Description: The `get_gas_value` function retrieves the gas value for a specific payment record number from the payments dictionary.
   - Arguments:
     - `nr` (int): The number of the apartment to retrieve values from.
     - `payments` (dict): A dictionary of all payments.
   - Returns: The gas value.

10. **get_water_value(nr, payments)**
    - Description: The `get_water_value` function retrieves the water value for a specific payment record number from the payments dictionary.
    - Arguments:
      - `nr` (int): The number of the apartment to retrieve values from.
      - `payments` (dict): A dictionary of all payments.
    - Returns: The water value.

11. **get_heat_value(nr, payments)**
    - Description: The `get_heat_value` function retrieves the heat value for a specific payment record number from the payments dictionary.
    - Arguments:
      - `nr` (int): The number of the apartment to retrieve values from.
      - `payments` (dict): A dictionary of all payments.
    - Returns: The heat value.

12. **get_sewage_value(nr, payments)**
    - Description: The `get_sewage_value` function retrieves the sewage value for a specific payment record number from the payments dictionary.
    - Arguments:
      - `nr` (int): The number of the apartment to retrieve values from.
      - `payments` (dict): A dictionary of all payments.
    - Returns: The sewage value.

13. **get_misc_value(nr, payments)**
    - Description: The `get_misc_value` function retrieves the misc value for a specific payment record number from the payments dictionary.
    - Arguments:
      - `nr` (int): The number of the apartment to retrieve values from.
      - `payments` (dict): A dictionary of all payments.
    - Returns: The misc value.

14. **get_date_value_str(nr, payments)**
    - Description: The `get_date_value_str` function retrieves the date value as a string for a specific payment record number from the payments dictionary.
    - Arguments:
      - `nr` (int): The number of the apartment to retrieve values from.
      - `payments` (dict): A dictionary of all payments.
    - Returns: The date value as a formatted string.

15. **get_total_value(nr, payments)**
    - Description: The `get_total_value` function calculates the total for a specific payment record number from the payments dictionary.
    - Arguments:
      - `nr` (int): The number of the apartment to retrieve values from.
      - `payments` (dict): A dictionary of all payments.
    - Returns: The total value.

16. **key_selector()**
    - Description: The `key_selector` function prompts the user to select a key (e.g., 'gas', 'water', 'heat', 'sewage', 'misc') and returns the selected key based on the user's input.
    - Arguments: None
    - Returns: The

 selected key as a string based on the user's input.

17. **read_float(msg: str)**
    - Description: The `read_float` function prompts the user to input a float value and handles any input errors.
    - Arguments:
      - `msg` (str): The message to display as a prompt to the user.
    - Returns: A float value entered by the user.

18. **read_int(msg: str)**
    - Description: The `read_int` function prompts the user to input an int value and handles any input errors.
    - Arguments:
      - `msg` (str): The message to display as a prompt to the user.
    - Returns: An int value entered by the user.

19. **read_date()**
    - Description: The `read_date` function prompts the user to input a date or autocompletes with today's date and handles any input errors.
    - Arguments: None
    - Returns: A date entered by the user.

20. **input_payment(payments: dict, changes: list)**
    - Description: The `input_payment` function allows the user to input payment information and updates the 'payments' dictionary.
    - Arguments:
      - `payments` (dict): A dictionary of all payments.
      - `changes` (list): A list where changes are recorded.
    - Returns: Nothing

21. **print_ap(payments, nr)**
    - Description: The `print_ap` function prints all the payments from an apartment.
    - Arguments:
      - `payments` (dict): A dictionary of all payments.
      - `nr` (int): The number of the apartment to retrieve values from.
    - Returns: Nothing

22. **print_grt(payments, value)**
    - Description: The `print_grt` function prints all the apartments with payments greater than a value.
    - Arguments:
      - `payments` (dict): A dictionary of all payments.
      - `value` (float): The value for comparison.
    - Returns: Nothing

23. **print_all_key(payments, key)**
    - Description: The `print_all_key` function displays payment information for a specific key (e.g., 'gas', 'water', 'heat') from all apartments.
    - Arguments:
      - `payments` (dict): A dictionary containing payment information for multiple apartments.
      - `key` (str): The payment category to be displayed (e.g., 'gas', 'water', 'heat').
    - Returns: Nothing

24. **total_by_key(payments, key)**
    - Description: The `total_by_key` function displays the total sum for a specific key (e.g., 'gas', 'water', 'heat') for all apartments.
    - Arguments:
      - `payments` (dict): A dictionary containing payment information for multiple apartments.
      - `key` (str): The payment category to be displayed (e.g., 'gas', 'water', 'heat').
    - Returns: Nothing

25. **del_under_value()**
    - The del_under_value function iteratively modifies payment information under a certain value and records a 'mMOD' operation in the changes list to indicate the mass modification.
    - Arguments:
         - `payments` (dict): A dictionary of all payments.
         - `value` (float): The value for comparison.
         - `changes` (list): A list where changes are recorded.
    - Returns: None

26. **auto_testing()**
    - Description: The `auto_testing` function automatically runs tests in a sandbox environment using random values to test various functions in your program.
    - Arguments: None
    - Returns: None
  
### Running scenario

| User                 	| Program                                         	| Description                                             	|
|----------------------	|-------------------------------------------------	|---------------------------------------------------------	|
|                      	| Displays menu                                   	| Awaits an input from the user                           	|
| 1                    	|                                                 	| Awaits apartment number                                 	|
| 101 and payment data 	| Awaits payment details                          	| Awaits payment details for Apartment 101 from the user  	|
| 1                    	|                                                 	| Awaits apartment number                                 	|
| 102 and payment data 	| Awaits payment details                          	| Awaits payment details for Apartment 102 from the user  	|
| 1                    	|                                                 	| Awaits apartment number                                 	|
| 103 and payment data 	| Awaits payment details                          	| Awaits payment details for Apartment 103 from the user  	|
| 2                    	| Displays submenu                                	| Awaits choice from user                                 	|
| 2                    	| Awayits start and end positions for delet       	| Asks user for the indexes from where to delete the data 	|
| 102 103              	| Deletes entries from 102 to 103                 	| The only entry remaining is 101                         	|
| 4                    	| Display menu                                    	| User exited submenu                                     	|
| 4                    	| Displays submenu                                	| Awaits choice from user                                 	|
| 3                    	| Enter apartment number:                         	| Asks user for an apartment to calculate the total for   	|
| 101                  	| Displays total value of the payments for ap 101 	|                                                         	|
| 4                    	| Display menu                                    	| User exited submenu                                     	|
| 7                    	| Exits                                           	| User exited the program                                 	|
