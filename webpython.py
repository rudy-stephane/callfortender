import os, os.path
import random
import string
import cherrypy
import datetime
import requests
import lxml
import cssselect
import lxml.html
import datetime
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.MIMEBase import MIMEBase
from pprint import pprint



class Data(object):
    def __init__(self,title,description,link):
        self.title = title
        self.description = description
        self.link = link
class SendMail(object):
    def __init__(self):
        print('envoi de mail')
    def methodetest(self):
        print('je suis dans la méthode test')

class MonSiteWeb(object):

    global htmlsite
    global variable
    global tabtitle
    global tabdesc
    global tablink
    global tabind
    #global tabdata
    global listededonnee
    

    def methodetest(self):
        print('je suis dans la méthode test')

        
    @cherrypy.expose
    def index(self):

        now = datetime.datetime.now()
        entetesite = ''' <!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Appel d'offre</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/bootstrap-3.3.7-dist/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/static/bootstrap-3.3.7-dist/css/scrolling-nav.css" rel="stylesheet">
	
	<link rel="stylesheet" type="text/css" href="/static/bootstrap-3.3.7-dist/DataTables/datatables.min.css"/>

  </head>

  <body id="page-top">

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand js-scroll-trigger" href="#page-top"><h4>Socitech</h4></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="#about">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="#services">Ajouter un filtre</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="methodetest">Action</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <header class="bg-primary text-white">
      <div class="container text-center">
        <h1> Appel d'offre venant du site global tender</h1>
        <p class="lead">resultat du "data scraping" du site global tender</p>
      </div>
    </header>

    <section id="about">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-12 mx-auto">
            <h2>Resultat de la recherche</h2>
			<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalLong">
				Envoi de la selection
			</button>
            <table id="example" class="display" style="width:100%">
			<thead><tr><th>Date</th><th>Title</th><th>Description</th><th>Link</th></tr></thead>
			<tbody>'''
        table = "<tr><td>{}</td><td>{}</td><td>{}</td><td><a href=\"{}\">{} </a></td></tr>"

        
        footer = '''
			</tbody></table>
          </div>
        </div>
      </div>
    </section>
	
	
	
	
	<div class="modal fade" id="exampleModalLong" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
			<div class="modal-header">
				<h5 class="modal-title" id="exampleModalLongTitle">Contacts</h5></br>
				<button type="button" class="close" data-dismiss="modal" aria-label="Close">
					<span aria-hidden="true">&times;</span>
				</button>
			</div>
			<div class="modal-body">
				<p>Ajoujer un Contact</p></br>
				<form>
				<div class="form-row">
					<div class="col-lg-6">
						<label for="name">Name :</label>
						<input type="text" class="form-control" id="name" placeholder="Name"  required>
					</div>
					<div class="col-lg-6">
						<label for="email">Email : </label>
						<input type="email" class="form-control" id="email" placeholder="EMAIL"  required>
					</div>
					<div class="col-lg-6">
						<label for="telephone">Telephone :</label>
						<input type="tel" class="form-control" id="telephone" placeholder="Telephone"  required>
					</div></br>
					<div class="col-lg-10">
						</br>
						<button type="button" class="btn btn-primary" id="addContact">Add Contacts</button>
					</div>
				</div>
				</form>
				<hr/>
				<table id="adresse" class="display" style="width:100%">
				<thead>
					<tr><th>NOMS</th><th>EMAIL</th><th>NUMERO</th></tr>
				</thead>
				<tbody>
					<tr><td>Rudy</td><td>rudy@yahoo.fr</td><td>671402318</td></tr>
				</tbody>
			</table>
			</div>
			<div class="modal-footer">
				<button id="moveContact" type="button" class="btn btn-primary">move selected row</button>
				<button id="sendEmail" type="button" class="btn btn-primary">send to selected row</button>
				<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
			</div>
		</div>
	</div>
</div>

    <!-- Footer -->
    <footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; Your Website 2017</p>
      </div>
      <!-- /.container -->
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="/static/bootstrap-3.3.7-dist/vendor/jquery/jquery.min.js"></script>
    <script src="/static/bootstrap-3.3.7-dist/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="/static/bootstrap-3.3.7-dist/vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom JavaScript for this theme -->
    <script src="/static/bootstrap-3.3.7-dist/js/scrolling-nav.js"></script>
	<script type="text/javascript" src="/static/bootstrap-3.3.7-dist/DataTables/datatables.min.js"></script>
	<script type="text/javascript" charset="utf-8">
                        $(document).ready(function() {

                                var titre = '' ;
                                var description = '' ;
                                var lien = '' ;

                                var olien = "" ;

                                function Object(titre, description, lien) {
                                    this.titre = titre;
                                    this.description = description;
                                    this.lien = lien;
                                }

                                var init = '' ;
                                var end = '' ;

                                function Add(init,end){
                                    this.init = init;
                                    this.end = end;
                                }
                                
				var table = $('#example').DataTable();
				
				$('#example tbody').on( 'click', 'tr', function () {
					$(this).toggleClass('selected');
				} );

				$('#adresse tbody').on( 'click', 'tr', function () {
					$(this).toggleClass('selected');
				} );

				$('#addContact').click( function () {
					var nom = $('#name').val();
					var email = $('#email').val();
					var telephone = $('#telephone').val();
					var usertable = $('#adresse').DataTable();
					if(nom!='' && email!='' && telephone!=''){
						usertable.row.add( [
							nom,
							email,
							telephone,
						] ).draw( false );
					}
				} );

				$('#moveContact').click( function () {
					
					//alert(nom + '  ' +  email + '  ' + telephone );
					var usertable = $('#adresse').DataTable();
					var rows = usertable.rows( '.selected' ).data();
					var indice ;
					var ttt = '' ;
					for(indice = 0 ; indice < rows.length ; indice++ )
							usertable.rows( '.selected' ).remove().draw();
							
				});

				$('#sendEmail').click(function (){
                                    var jsontable = $('#example').DataTable();
                                    var jsontableaddresse = $('#adresse').DataTable();
                                    var rows = jsontable.rows( '.selected' ).data();
                                    var rowsaddresse = jsontableaddresse.rows( '.selected' ).data();
                                    var indice ;
                                    var indiceaddresse ;
                                    var object ={};
                                    var add = {} ;
                                    var tabObject ={};
                                    var tabaddresse = {};

                                    //liste des addresses où iront les donnees
                                    var test = rowsaddresse[0][1] ;

                                    for(indiceaddresse = 0 ; indiceaddresse < rowsaddresse.length ; indiceaddresse++){

                                        var chn = rowsaddresse[indiceaddresse][1] ;
					var aropos = chn.indexOf('@') ;
					var init = chn.slice(0,aropos) ;
					var end = chn.slice(aropos+1) ;

                                        add = new Add(init,end);
                                            
                                        tabaddresse[indiceaddresse] = add;

                                    }

                                    var jsoAd = JSON.stringify(tabaddresse);
                                    var eltselectAd = rowsaddresse.length ;

                                    //liste des donnees a envoyer

                                    for(indice = 0 ; indice < rows.length ; indice++){

                                        var str = String(rows[indice][3]) ;
                                        var nstr = str.substr(156) ;
                                        var chn = nstr.slice(0,9) ;
                                        object = new Object(rows[indice][1],rows[indice][2],chn);

                                        tabObject[indice] = object ;

                                    }
                                    var resultat = {};
                                    resultat['valeur'] = tabObject ;
                                    var eltselect = rows.length ;

                                    var jsO = JSON.stringify(tabObject); //{"action":"valeur"};//tabObject
                                    
                                    $.ajax({
                                            url : 'sendMail',
                                            type : 'POST',
                                            dataType: 'application/json',
                                            data : 'donnee=' + jsO + '&qtdonnee=' + eltselect + '&addresse=' + jsoAd + '&qtAddonnee=' + eltselectAd,
                                            success : function(code, statut){

                                                $('#exampleModalLong').modal('hide');

                                            },

                                            error : function(resultat, statut, erreur){

                                            },

                                            complete : function(resultat, statut){

                                                $('#exampleModalLong').modal('hide');

                                           }
                                        });
				});

						
			} );	
	</script>
	<script type="text/javascript">
	// For demo to fit into DataTables site builder...
	$('#example')
		.removeClass( 'display' )
		.addClass('table table-striped table-bordered');
		
	$('#adresse')
		.removeClass( 'display' )
		.addClass('table table-striped table-bordered');
	
        </script>

  </body>

</html>

'''
        tabtitle = []
        tabdesc = []
        tablink = []
        tabind = []
        global tabdata
        
        txt = 'ma variable'
        indice = 0
        url = 'https://www.globaltenders.com/tenders-cameroon.php'
        while(url !='#'):
            reponse = requests.get(url)#'http://www.globaltenders.com/'
            tree = lxml.html.fromstring(reponse.text)
            tdElems = tree.xpath('//table/tr/td[@style="width:70%; vertical-align:top; text-align:left;"]')#|//table/tr/td/a/@href
            tdElink = tree.xpath('//table/tr/td/a/@href')
            taille = len(tdElems)
            indice = 0
            intitule =''
            adresse = ''
            mylist = list()
            mydescription = list()
            mytitle = list()
            listData = list()
            while (indice < taille):
                if(tdElems[indice].text_content() == ' Technology Hardware and Equipment'):
                    ltail = indice//2
                    intitule = ' Technology Hardware and Equipment'
                    adresse = tdElink[ltail]
                    mylist.append(adresse)
                    val = indice+1
                    mydescription.append(tdElems[val].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[val].text_content(),adresse)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                    #print(adresse)
                elif(tdElems[indice].text_content() == ' Smart Cards and other Access Control system , Printing and publishing'):

                    ltailt = indice//2
                    intitulet = tdElems[indice].text_content()
                    adresset = tdElink[ltailt]
                    mylist.append(adresset)
                    val = indice+1
                    mydescription.append(tdElems[val].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[val].text_content(),adresset)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                    #print(adresset)
        
                elif(tdElems[indice].text_content() == ' Software Services'):

                    ltailf = indice//2
                    intitulef = tdElems[indice].text_content()
                    adressef = tdElink[ltailf]
                    mylist.append(adressef)
                    val = indice+1
                    mydescription.append(tdElems[val].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[val].text_content(),adressef)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                    #print(adressef)
        
                elif(tdElems[indice].text_content() == ' Bridges and Tunnels'):

                    ltails = indice//2
                    intitules = tdElems[indice].text_content()
                    adresses = tdElink[ltails]
                    mylist.append(adresses)
                    val = indice+1
                    mydescription.append(tdElems[val].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[val].text_content(),adresses)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                    #print(adresses)
        
                elif(tdElems[indice].text_content() == ' Services'):

                    ltailn = indice//2
                    intitulen = tdElems[indice].text_content()
                    adressen = tdElink[ltailn]
                    mylist.append(adressen)
                    val = indice+1
                    mydescription.append(tdElems[val].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[val].text_content(),adressen)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                    #print(adressen)
        
                elif(tdElems[indice].text_content() == ' Printing and publishing'):

                    ltailk = indice//2
                    intitulek = tdElems[indice].text_content()
                    adressek = tdElink[ltailk]
                    mylist.append(adressek)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adressek)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                    #print(adressek)
        
                elif(tdElems[indice].text_content() == ' Industry , Technology Hardware and Equipment , Furniture'):

                    ltaily = indice//2
                    intituley = tdElems[indice].text_content()
                    adressey = tdElink[ltaily]
                    mylist.append(adressey)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adressey)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                    #print(adressey)
                elif(tdElems[indice].text_content() == ' Telecommunications , Information Technology (IT) , Consultancy , Services , Infrastructure and construction'):
                    ltaill = indice//2
                    intitulel = tdElems[indice].text_content()
                    adressel = tdElink[ltaill]
                    mylist.append(adressel)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adressel)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                    #print('*****************')
            
                elif(tdElems[indice].text_content() == ' Industry , Technology Hardware and Equipment'):

                    ltailycp = indice//2
                    intituleycp = tdElems[indice].text_content()
                    adresseycp = tdElink[ltailycp]
                    mylist.append(adresseycp)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adresseycp)
                    listData.append(data)
                    print(tdElems[indice].text_content())
            
                elif(tdElems[indice].text_content() == ' Telecommunications'):

                    ltailytele = indice//2
                    intituleytele = tdElems[indice].text_content()
                    adresseytele = tdElink[ltailytele]
                    mylist.append(adresseytele)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adresseytele)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                    
                elif(tdElems[indice].text_content() == ' Technology Hardware and Equipment , Energy, Power and Electrical'):

                    ltailyHard = indice//2
                    intituleyHard = tdElems[indice].text_content()
                    adresseyHard = tdElink[ltailyHard]
                    mylist.append(adresseyHard)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adresseyHard)
                    listData.append(data)
                    print(tdElems[indice].text_content())

                elif(tdElems[indice].text_content() == ' Telecommunications , Banking, Finance, Insurance and Securities (BFIS) , Information Technology (IT) , Consultancy'):

                    ltailyBank = indice//2
                    intituleyBank = tdElems[indice].text_content()
                    adresseyBank = tdElink[ltailyBank]
                    mylist.append(adresseyBank)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adresseyBank)
                    listData.append(data)
                    print(tdElems[indice].text_content())

                elif(tdElems[indice].text_content() == ' Telecommunications , Information Technology (IT) , Consultancy , Infrastructure and construction , Building'):

                    ltailyInfor = indice//2
                    intituleyInfor = tdElems[indice].text_content()
                    adresseyInfor = tdElink[ltailyInfor]
                    mylist.append(adresseyInfor)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adresseyInfor)
                    listData.append(data)
                    print(tdElems[indice].text_content())

                elif(tdElems[indice].text_content() == ' Telecommunications , Information Technology (IT) , Software Services , Consultancy'):

                    ltailymunic = indice//2
                    intituleymunic = tdElems[indice].text_content()
                    adresseymunic = tdElink[ltailymunic]
                    mylist.append(adresseymunic)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adresseymunic)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                    
                elif(tdElems[indice].text_content() == ' Telecommunications , Infrastructure and construction'):

                    ltailyInfras = indice//2
                    intituleyInfras = tdElems[indice].text_content()
                    adresseyInfras = tdElink[ltailyInfras]
                    mylist.append(adresseyInfras)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adresseyInfras)
                    listData.append(data)
                    print(tdElems[indice].text_content())

                elif(tdElems[indice].text_content() == ' Telecommunications , Information Technology (IT) , Consultancy'):

                    ltailyConsul = indice//2
                    intituleyConsul = tdElems[indice].text_content()
                    adresseyConsul = tdElink[ltailyConsul]
                    mylist.append(adresseyConsul)
                    mydescription.append(tdElems[indice+1].text_content())
                    mytitle.append(tdElems[indice].text_content())
                    data = Data(tdElems[indice].text_content(),tdElems[indice+1].text_content(),adresseyConsul)
                    listData.append(data)
                    print(tdElems[indice].text_content())
                
                 
                indice = indice + 1
                tabtitle = tabtitle + mytitle
                #tabtitle = mytitle
                tabdesc  = tabdesc + mydescription
                #tabdesc = mydescription
                tablink  = tablink + mylist
                #tablink = mylist
                tabdata = listData
                
                
            #tabdata = listData
            #tabind = 
            #print(listData,'*********************')
            tdElemslm = tree.xpath('//select[@style="float:left"]')
            mlistlm = tdElemslm[0].getnext().getchildren()
            if len(mlistlm) == 2 :
                #print(mlistlm[1].xpath('@href')[0])
                adressederedirection = mlistlm[1].xpath('@href')[0]
            else :
                #print(mlistlm[0].xpath('@href')[0])
                if(mlistlm[0].text_content() == 'Next Page'):
                    adressederedirection = mlistlm[0].xpath('@href')[0]
                else:
                    adressederedirection = '#'
            url= adressederedirection
            

        #global listData
        #listData = list()
        listededonnee = list()
        nlisted = list()
        inlist=0
        while inlist < len(tabtitle):
            donnee = Data(tabtitle[inlist],tabdesc[inlist],tablink[inlist])
            listededonnee.append(donnee)
            inlist = inlist+1
        print(listededonnee)
        print(len(listededonnee),'/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-')

        for donnee in listededonnee :
            c = 0
            nindic = 1
            lesindices = []
            listedesdons = listededonnee
            while nindic < len(listededonnee):
                if donnee.title == listededonnee[nindic].title and donnee.description == listededonnee[nindic].description and donnee.link == listededonnee[nindic].link:
                    c = c+1
                    if(c>0):
                       listededonnee.remove(listededonnee[nindic])  
                nindic = nindic + 1
            print(c)
            
        print(listededonnee)
        print(len(listededonnee),'/*-+/*-+/*-+/*-+/*-+/*-+/*-+/*-+/*-+/*-+/*-+/*-+/*-+')

        #listData = listededonnee

        for el in listededonnee :
            inc = 0
            indel = 0
            while indel < len(listededonnee):
                if el.title == listededonnee[indel].title and el.description == listededonnee[indel].description and el.link == listededonnee[indel].link:
                    inc = inc + 1
                    if inc >1 :
                        listededonnee.remove(listededonnee[indel]) 
                indel = indel + 1
        for iii in listededonnee :
            print(iii.title)

        pagehtml = ''
        for td in listededonnee :
            pagehtml = pagehtml + table.format(str(now),td.title,td.description,td.link,td.link)

        return entetesite + pagehtml + footer

    @cherrypy.expose
    def sendMail(self,donnee,qtdonnee,addresse,qtAddonnee):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        variable = r"""{}"""
        data = json.loads(variable.format(donnee))
        print(data,'+/++/+/++/++/++/++/++/*+/+*/+*/+*/+*/+*/+*/+*/')
        print('---------------------------------------------------')
        indice = 0
        message = """
                    <!DOCTYPE html>
                        <html lang="fr">
                        <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <meta name="description" content="">
                                <meta name="author" content="">
                                <title>Appel d'offre</title>

                                <!-- Bootstrap core CSS -->
                                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
                                
                        </head>
                     <body>
                         <table id="example" style="width:100%; border-collapse: collapse;" class="table table-bordered">
                            <thead >
                                <tr><th>Title</th><th>Description</th><th>Link</th></tr>
                            </thead>
                            <tbody>"""
        tdata = """<tr><td>{}</td><td>{}</td><td><a href=\"{}\">lien du site</a></td></tr>"""
                        
        fin = """
                            </tbody>
                        </table>
                        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>
                        </body>
                    </html>
                    """
        valdonnee = ''
        while indice < int(qtdonnee) :
            chn = str(indice)
            valdonnee = valdonnee + tdata.format(data[chn]['titre'],data[chn]['description'],'http://www.globaltenders.com/auth-tenders.php?action=details&id='+data[chn]['lien'])
            indice = indice + 1

        
        indicead = 0
        variablead = r"""{}"""
        address = json.loads(variable.format(addresse))
        lAd = list()
        while indicead < int(qtAddonnee) :
           chn = str(indicead)
           valAd = address[chn]['init']+'@'+ address[chn]['end']
           lAd.append(valAd)
           print(valAd)
           indicead = indicead + 1

        MessageSending = message + valdonnee +fin
        indiceMail = 0
        me = 'tekamfossi@gmail.com'
        text = "Appel d'offre !"
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(MessageSending, 'html')
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Appel d'offre"
        msg['From'] = me
        msg.attach(part1)
        msg.attach(part2)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(me, "degrace1")
        while indiceMail < len(lAd):
            msg['To'] = lAd[indiceMail] 
            server.sendmail(me, lAd[indiceMail], msg.as_string())
            indiceMail = indiceMail + 1
        server.quit()
        lstre = {}
        lstre['resultat'] = 'ok'
        return ''
    
    #index.exposed = True

    #methodetest.exposed = True

    #sendMail.exposed = True

cherrypy.quickstart(MonSiteWeb(), config ="server.conf")
