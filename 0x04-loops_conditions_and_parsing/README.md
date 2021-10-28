0x04. Loops, conditions and parsing
 By Sylvain Kalache
 Ongoing project - started 10-28-2021, must end by 10-29-2021 (in about 16 hours) - you're done with 107% of tasks.
 Checker was released at 10-28-2021 02:23 PM
 QA review fully automated.
About Bash projects
Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

Background Context


Resources
Read or watch:

Loops sample
Variable assignment and arithmetic
Comparison operators
File test operators
Make your scripts portable
man or help:

env
cut
for
while
until
if
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to create SSH keys
What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
How to use while, until and for loops
How to use if, else, elif and case condition statements
How to use the cut command
What are files and other comparison operators, and how to use them
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
You are not allowed to use awk
Your Bash script must pass Shellcheck (version 0.7.0) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
More Info
Shellcheck
Shellcheck is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

Shellcheck is available on the school’s computers. If you want to use it on your own computer, here is how to install it.

Examples:

Not passing Shellcheck:



Passing Shellcheck:



For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code SC2034, you can browse https://github.com/koalaman/shellcheck/wiki/SC2034.

Tasks
0. Create a SSH RSA key pair
mandatory
Read for this task:

Linux and Mac OS users
Windows users
man: ssh-keygen

You will soon have to manage your own servers concept page hosted on remote data centers. We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:

Share your public key in your answer file 0-RSA_public_key.pub
Fill the SSH public key field of your intranet profile with the public key you just generated
Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase
SSH and RSA keys will be covered in depth in a later project.

Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 0-RSA_public_key.pub
For Best School loop
mandatory
rite a Bash script that displays Best School 10 times.
Requirement:
You must use the for loop (while and until are forbidden)
ad -n 2 1-for_best_school 
#!/usr/bin/env bash
# This script is displaying "Best School" 10 times
sylvain@ubuntu$ ./1-for_best_school 
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
Note that:

The first line of my Bash script starts with #!/usr/bin/env bash
The second line of my Bash scripts is a comment explaining what it is doing
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 1-for_best_school
   
2. While Best School loop
mandatory
Write a Bash script that displays Best School 10 times.

Requirements:

You must use the while loop (for and until are forbidden)
sylvain@ubuntu$ ./2-while_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 2-while_best_school
   
3. Until Best School loop
mandatory
Write a Bash script that displays Best School 10 times.

Requirements:

You must use the until loop (for and while are forbidden)
sylvain@ubuntu$ ./3-until_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 3-until_best_school
   
4. If 9, say Hi!
mandatory
Write a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.

Requirements:

You must use the while loop (for and until are forbidden)
You must use the if statement
sylvain@ubuntu$ ./4-if_9_say_hi
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Hi
Best School
sylvain@ubuntu$ 
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 4-if_9_say_hi
   
5. 4 bad luck, 8 is your chance
mandatory
Write a Bash script that loops from 1 to 10 and:

displays bad luck for the 4th loop iteration
displays good luck for the 8th loop iteration
displays Best School for the other iterations
Requirements:

You must use the while loop (for and until are forbidden)
You must use the if, elif and else statements
sylvain@ubuntu$ ./5-4_bad_luck_8_is_your_chance
Best School
Best School
Best School
bad luck
Best School
Best School
Best School
good luck
Best School
Best School
sylvain@ubuntu$ 
For the most curious:

8 in the Chinese culture
4 in the Chinese culture
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 5-4_bad_luck_8_is_your_chance
   
6. Superstitious numbers
mandatory
Write a Bash script that displays numbers from 1 to 20 and:

displays 4 and then bad luck from China 