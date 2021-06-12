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
   "execution_count": 7,
   "id": "1144348d-e063-4ea6-9683-74fb374118a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The total number of months included in the report are 86\n"
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
    "total_months = len(budget_report)\n",
    "\n",
    "print(f\"The total number of months included in the report are {total_months}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "624ccfff-9e07-4aa7-b60c-623c7dc1257a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'datetime' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-11-b77e444139ac>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Trying to count the month using datetime by attributing the start_date and the end_date as found on kite.com\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mstart_date\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdatetime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2010\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0mend_date\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdatetime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2017\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'datetime' is not defined"
     ]
    }
   ],
   "source": [
    "# Trying to count the month using datetime by attributing the start_date and the end_date as found on kite.com \n",
    "\n",
    "start_date = datetime.datetime(2010,1)\n",
    "end_date = datetime.datetime(2017,2)\n",
    "\n",
    "num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)\n",
    "\n",
    "print(num_months)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94fe0bb4-40a7-4702-92b3-c56fa37d1df9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyze the records to print the total number of monthe included in the dataset\n"
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
