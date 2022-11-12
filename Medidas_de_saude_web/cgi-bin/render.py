def template_tela(data):
        print("Content-type:text/html\r\n\r\n")
        print("""
            
                <html>
                    <head>
                        
                        <title>Medidas de saúde</title>
                        
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
                        <link rel="stylesheet" href="../style.css">

                    </head>

                    <body>
                        <div class="text-center">
                            <h5>Medidas de saúde</h5>

                            <h3>RESULTADO</h3>
                        </div>
                        <div class="container px-4">
                            <div class="row gx-5 justify-content-md-center">
                                <div class="col-5 ">
                                    <div class="p-3 {} rounded">
                                        <div class="text-center">
                                                <h2>{}</h2> <br><br>

                                        </div>
                                        
                                        <div>
                                            <form class="form-group" action="../index.html">
                                                

                                                <div align="center">    
                                                    <input type="submit" class="btn btn-light" value="Realizar novo cálculo">
                                                </div>

                                            </form>   
                                        </div>                  
                                    </div>
                                </div>
                            
                            </div>
                        </div>
                        

                    </body>
                </html>""".format(data[0], data[1]))      
