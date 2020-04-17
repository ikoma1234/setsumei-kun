title = "aiueo"
setsumei = "a\nb\nc\n"

honbun = setsumei.replace("\n", "<br>")

if(title!="" and setsumei!=""):

    pc="<tr>\n  <td width=\"154\" align=\"center\">"+ title +"</td>\n   <td width=\"675\"><br>"+ honbun + "</td>    </tr>"
    
    smapho="【"+title+"】<br>"+honbun+"<br>"
    
    print(pc)
    print(smapho)

