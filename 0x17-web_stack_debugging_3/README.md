# 0x17. Web stack debugging #3

## Description
What you should learn from this project:
* Application of tmux, and strace
---

### [0. Strace is your friend](./0-strace_is_your_friend.pp)
*  To run strace in one window and curl in another one
Requirements:

Your 0-strace_is_your_friend.pp file must contain Puppet code
You can use whatever Puppet resource type you want for you fixUsing strace, find out why Apache is returning a 500 error.
Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

Hint:

	* strace can attach to a current running process
	* You can use tmux to run strace in one window and curl in another one

---

## Author
* **Habtamu B Mekonnen** 
