%import json
%import bottle
%skra=open('bekkur.json','r',encoding='UTF-8')
%l=json.load(skra)

% for i in l['nemendur']:
     kennitala:<a href="/nemandi/{{i['kt']}}">{{i['kt']}}</a><br>
     Nafn: {{i['nafn']}}<br>
     Braut: {{i['braut']}}<br>
% end




