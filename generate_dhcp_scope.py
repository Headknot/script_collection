# -*- coding: utf-8 -*-

def main():
    for i in range(0, 201):
        template = """
        subnet 10.1.{0}.0 netmask 255.255.255.0 {{
          option routers 10.1.{0}.1;
          option domain-name-servers 217.13.225.101, 217.13.225.121;
          option broadcast-address 10.1.{0}.255;
          pool {{
		   failover peer "failover-partner";
           range 10.1.{0}.10 10.1.{0}.200;
          }}
        }}""".format(i)
        print(template)

        with open("output.txt", "a") as myfile:
            myfile.write(template)
        

if __name__ == "__main__":
	main()
