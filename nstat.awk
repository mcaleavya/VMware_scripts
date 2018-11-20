BEGIN { printf ("%-12s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s\n","TSTAMP","IFACE","rxpck\/s","txpck\/s","rxMB\/s","txMB\/s","rxsize","txsize","rxeps","txeps");}
 {
 if ( $0 ~ /time / ) { ts=$2;}
 if ( $0 ~ /vmnic/ )
 {
 vmnic=$2;
 found=1;
 }
 if (( $0 ~ /txpps/ ) && ( found == 1))
 {
 printf("%-12s %-8s %-8d %-8d %-8.2f %-8.2f %-8d %-8d %-8d %-8d \n",strftime("%r",ts),vmnic,$10,$2,$12/8,$4/8,$14,$6,$NF,$8);
 found=0;
 }
 }
