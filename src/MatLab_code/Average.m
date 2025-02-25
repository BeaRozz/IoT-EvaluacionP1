% Define el ID de tu canal de ThingSpeak
channelIDWrite = 0; %Id del canal donde se escribe
channelIDRead = 1; %Id del canal donde se obtienen los datos

% Define el API key de escritura (Write API Key)
writeAPIKey = 'WRITE_API_KEY'; 

% Define el API key de lectura (Read API Key)
readAPIKey = 'READ_API_KEY';

% Lee 10 datos del campo 1 del canal de lectura
data = thingSpeakRead(channelIDRead, 'Field', 1, 'NumPoints', 10, 'ReadKey', readAPIKey);

%Filtra los datos que sean nulos o NaN
data = data(~isnan(data));

% Calcula el promedio de los últimos 10
averageData = mean(data);

% Escribe el promedio en el field 2 del canal de escritura
thingSpeakWrite(channelIDWrite, averageData, 'Field', 2, 'WriteKey', writeAPIKey);

%Imprime los datos
disp(data)