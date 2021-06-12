{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "55bc1533-3f70-4f02-ae3a-9f4bc29304af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"\\nUnit 1 | Automate my Day Job using Python\\n\\n1. Load .csv File using Pandas in order to read the data for the necessary output. \\n    1.1 Load the Pandas libraries with alias 'pd data = pd.\\n    1.2 Import pandas as pd.\\n    1.3 Read data from file 'filename.csv'\\n    1.4 In the same directory that your python process is based\\n\\n\""
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "Unit 1 | Automate my Day Job using Python\n",
    "\n",
    "1. Load .csv File using Pandas in order to read the data for the necessary output. \n",
    "    1.1 Load the Pandas libraries with alias 'pd data = pd.\n",
    "    1.2 Import pandas as pd.\n",
    "    1.3 Read data from file 'filename.csv'\n",
    "    1.4 In the same directory that your python process is based\n",
    "\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9f434f6e-d35c-4fef-acc3-b7bf6ae29cef",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load panda libraries with alias 'pd'\n",
    "\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "86735d54-67e8-4681-8958-9d58d05cddbf",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Read data from file 'budget_data.csv'\n",
    "# in the same directory as the python homework process\n",
    "\n",
    "data = pd.read_csv(\"budget_data.csv\")\n",
    "budget_report = data.values.tolist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1144348d-e063-4ea6-9683-74fb374118a7",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The total number of months included in the report are: 86 months\n"
     ]
    }
   ],
   "source": [
    "# To test that I can read the file without having to do another action\n",
    "\n",
    "len(\"budget_data.csv\") \n",
    "\n",
    "# Above output gave me 15 which is wrong. Going to try another function. Trying different by creating a variabel\n",
    "# called total_months\n",
    "\n",
    "\n",
    "total_months = len(budget_report)\n",
    "\n",
    "print(f\"The total number of months included in the report are: {total_months} months\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "190e279a-73a5-4181-9a1e-e4d267cddf63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Net P&L: $38382578\n"
     ]
    }
   ],
   "source": [
    "# Print the Net Total Amount of Profit and Loss over the entire over the entire period. \n",
    "\n",
    "net_total = data.iloc[:,1].sum()\n",
    "print(f\"Total Net P&L: ${net_total}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc736da8-a5dc-4392-936b-92bf70c03893",
   "metadata": {},
   "outputs": [],
   "source": [
    "# The average Profit & Loss Over the defined time period\n",
    "\n",
    "total_amount = budget_report[0][1]\n",
    "average_sum = 0.00\n",
    "previous_month = budget_report[0][1]\n",
    "previous_month_text = budget_report[0][0]\n",
    "greatest_increase = previous_month\n",
    "greatest_increase_text = previous_month_text\n",
    "greatest_loss_amount = 0\n",
    "\n",
    "for month in budget_report[1:]:\n",
    "    current_month_pl = month[1]\n",
    "    current_month_text = month[0]\n",
    "    \n",
    "    total_amount += current_month_pl\n",
    "    \n",
    "    different_between_months = current_month_pl - previous_month\n",
    "    average_sum += different_between_months\n",
    "    \n",
    "    previous_month = current_month_pl\n",
    "    previous_month_text = current_month_text\n",
    "    \n",
    "print(f\"Total amount loop: {total_amount})\n",
    "print(f\"The average Profit & Loss change is: {round(average_sum)})\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
