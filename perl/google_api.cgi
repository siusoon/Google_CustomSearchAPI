#!/opt/local/bin/perl   
use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser';
use LWP::UserAgent;
use JSON;
use warnings;                   
use JSON::API;
use JSON::Parse;
#my $ua = new LWP::UserAgent;  
my $ua = LWP::UserAgent->new;


print "Content-type: text/html\n\n";
print "<html><head><title>Hello World</title></head>\n";
print "<body>\n";
print "<h2>Hello, world!</h2>\n";

#### search criteria ####
my $api = "https://www.googleapis.com/customsearch/v1?";
my $key = 'input your own key';
my $cx = 'input your own engine ID';
my $q = 'NET+ART+GENERATOR';
my $searchType = 'image';
my $imgSize ='xxlarge';
my $url = $api . "key=" . $key . "&cx=" . $cx . "&q=" . $q . "&searchType=" . $searchType . "&imgSize=" . $imgSize;
#### End of search criteria ####


my $request = HTTP::Request->new("GET" => $url);
my $response = $ua->request($request);

if ($response->is_success) {
    my $message = $response->decoded_content;
    #print "Received reply: $message\n";
    my $json = new JSON;
    my $query = decode_json $message;
  	#print($query->{url}{type});
	my $extract1 = $query->{items};
    for my $pick (@$extract1) {
       #print $pick->{snippet}, "\n";
       #the list: items>0>pagemap>cse_thumbnail > 0 > src
       print "$pick->{image}->{thumbnailLink}";
       print "<p>";
       print "<img src='$pick->{image}->{thumbnailLink}'>";
       print "<p>";
	}

}
else {
    print "HTTP GET error code: ", $response->code, "\n";
    print "HTTP GET error message: ", $response->message, "\n";
}

print "</body></html>\n";