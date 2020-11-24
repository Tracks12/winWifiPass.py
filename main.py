#!/bin/python3
# -*- coding: utf-8 -*-

from subprocess import check_output as shell

def main():
	output = shell(["netsh", "wlan", "show", "profiles"]).decode("ansi").split("\n")
	wifis = [ line.split(":")[1][1:-1] for line in output if("Profil Tous les utilisateurs" in line) ]

	print("\n Wifi stored:\n ---- ------\n")

	for wifi in wifis:
		output = shell(["netsh", "wlan", "show", "profiles", wifi, "key=clear"]).decode("ansi").split("\n")
		password = [ line.split(":")[1][1:-1] for line in output if("Contenu de la cl" in line) ]

		try:
			print(f"  {wifi}{' '*(30-len(wifi))}: {password[0]}")

		except Exception:
			print(f"  {wifi}{' '*(30-len(wifi))}: -")

	return(True)

if(__name__ == "__main__"):
	main()
