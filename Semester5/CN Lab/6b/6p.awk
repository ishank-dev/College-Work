BEGIN{
	ftpsize = 0;
	cbrsize = 0;
	ftppkt = 0;
	cbrpkt = 0;
	ftptotal = 0;
	cbrtotal = 0;
}
{
	event = $1;
	pkttype = $5;
	pktsize = $6;
	if(pkttype == "tcp"){
		if(event == "r"){
		ftppkt++;
		ftpsize = pktsize;
		}
	}
	if(pkttype == "cbr"){
		if(event == "r"){
		cbrpkt++;
		cbrsize = pktsize;
		}
	}
}
END{
	ftptotal = ftppkt*ftpsize;
	cbrtotal = cbrpkt*cbrsize
	printf("Total throughput of FTP is %d bytes per second" ftptotal/24);
	printf("Total throughput of CBR is %d bytes per second" cbrtotal/24);
}


