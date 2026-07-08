/* Tested on Slackware linux with kernel 2.0.35 */

#include <fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h>
#include <ctype.h>
#include <arpa/nameser.h>
#include <sys/stat.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>

void main(int argc, char *argv[])
{
 int sock,debugm=0;
 struct in_addr addr;
 struct sockaddr_in sin;
 struct hostent *he;
 unsigned long start;
 unsigned long end;
 unsigned long counter;
 char foundmsg[] = "200";
 char *cgistr;
 char buffer[1024];
 int count=0;
 int numin;
 char cgibuff[1024];
 char *buff[50];    /* Don't u think 50 is enought? */
 char *cginame[50]; /* Don't u think 50 is enought? */

 buff[1] = "GET /cgi-bin/phf HTTP/1.0\n\n";
 buff[2] = "GET /cgi-bin/Count.cgi HTTP/1.0\n\n";
 buff[3] = "GET /cgi-bin/test-cgi HTTP/1.0\n\n";
 buff[4] = "GET /cgi-bin/php.cgi HTTP/1.0\n\n";
 buff[5] = "GET /cgi-bin/handler HTTP/1.0\n\n";
 buff[6] = "GET /cgi-bin/webgais HTTP/1.0\n\n";
 buff[7] = "GET /cgi-bin/websendmail HTTP/1.0\n\n";
 buff[8] = "GET /cgi-bin/webdist.cgi HTTP/1.0\n\n";
 buff[9] = "GET /cgi-bin/faxsurvey HTTP/1.0\n\n";
 buff[10] = "GET /cgi-bin/htmlscript HTTP/1.0\n\n";
 buff[11] = "GET /cgi-bin/pfdispaly.cgi HTTP/1.0\n\n";
 buff[12] = "GET /cgi-bin/perl.exe HTTP/1.0\n\n";
 buff[13] = "GET /cgi-bin/wwwboard.pl HTTP/1.0\n\n";

 cginame[1] = "phf";
 cginame[2] = "Count.cgi";
 cginame[3] = "test-cgi";
 cginame[4] = "php.cgi";
 cginame[5] = "handler";
 cginame[6] = "webgais";
 cginame[7] = "websendmail";
 cginame[8] = "webdist.cgi";
 cginame[9] = "faxsurvey";
 cginame[10] = "htmlscript";
 cginame[11] = "pfdisplay";
 cginame[12] = "perl.exe";
 cginame[13] = "wwwboard.pl";

 if (argc<2)
   {
   printf("\nusage : %s host ",argv[0]);
   printf("\n   Or : %s host -d   for debug mode\n\n",argv[0]); 
   exit(0);
   }

 if (argc>2)
   {
   if(strstr("-d",argv[2]))
     {
     debugm=1;
     }
   }

 if ((he=gethostbyname(argv[1])) == NULL)
   {
   herror("gethostbyname");
   exit(0);
   }

 printf("\n\n\t\t [CKS & Fdisk]'s CGI Checker\n\n\n");
 start=inet_addr(argv[1]);
 counter=ntohl(start);

   sock=socket(AF_INET, SOCK_STREAM, 0);
   bcopy(he->h_addr, (char *)&sin.sin_addr, he->h_length);
   sin.sin_family=AF_INET;
   sin.sin_port=htons(80);

  if (connect(sock, (struct sockaddr*)&sin, sizeof(sin))!=0)
     {
     perror("connect");
     }
   printf("\n\n\t [ Press any key to check out the httpd version...... ]\n");
   getchar(); 
   send(sock, "HEAD / HTTP/1.0\n\n",17,0);
   recv(sock, buffer, sizeof(buffer),0);
   printf("%s",buffer);
   close(sock); 
   printf("\n\t [ Press any key to search 4 CGI stuff...... ]\n");
   getchar();
   
while(count++ < 13)   /* Change 13 to how many buff[?] u have above */
   {
   sock=socket(AF_INET, SOCK_STREAM, 0);
   bcopy(he->h_addr, (char *)&sin.sin_addr, he->h_length);
   sin.sin_family=AF_INET;
   sin.sin_port=htons(80);
   if (connect(sock, (struct sockaddr*)&sin, sizeof(sin))!=0)
     {
     perror("connect");
     }
   printf("Searching for %s : ",cginame[count]);
  
   for(numin=0;numin < 1024;numin++)
      {
      cgibuff[numin] = '\0';
      } 
  
   send(sock, buff[count],strlen(buff[count]),0);
   recv(sock, cgibuff, sizeof(cgibuff),0);
   cgistr = strstr(cgibuff,foundmsg);
   if( cgistr != NULL)
       printf("Found !! ;)\n");
   else
       printf("Not Found\n");
      
  if(debugm==1)
    { 
    printf("\n\n ------------------------\n %s \n ------------------------\n",cgibuff); 
    printf("Press any key to continue....\n");
    getchar();
    }  
   close(sock);
   }
 }