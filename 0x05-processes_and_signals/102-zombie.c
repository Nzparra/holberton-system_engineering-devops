#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - create 5 zombie processes
 * Return: 0
 **/
int main(void)
{
	int c;
	pid_t pid;

	for (c = 0; c < 5; c++)
	{
		pid = fork();
		if (pid > 0)
		{
			sleep(1);
		}
		else
		{
			exit(0);
		}
		printf("Zombie process created, PID: %d\n", pid);
	}
	infinite_while();
	return (0);
}
