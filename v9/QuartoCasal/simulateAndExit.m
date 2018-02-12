% Initialize model variables
delTim    = 60*60;  % time step cada iteração, equal to one hour
TIni      = 10; % tempo inicial
tau       = 2*3600; % tempo final
%Q0Hea     = 100; % tempo abertura janela
%UA        = Q0Hea / 20;
%TOut      = 5; % tempo de movimentação da janela
%k=0;
% Initialize flags
retVal    = 0;
flaWri    = 0;
flaRea    = 0;
simTimWri = 0;
simTimRea = 0;

%inputs = [0 0 0 0];
inputs = [1 1 1];
%outputs = [0 0 0 0 0 0 0];
outputs = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Add path to BCVTB matlab libraries
addpath( strcat(getenv('BCVTB_HOME'), '/lib/matlab'));


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Establish the socket connection
sockfd = establishClientSocket('socket.cfg');
if sockfd < 0
    fprintf('Error: Failed to obtain socket file descriptor. sockfd=%d.\n', sockfd);
    exit;
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Loop for simulation time steps.
simulate = 1;
tcp = tcpip('localhost', 50032);
fopen(tcp);

while (simulate)
    % Assign values to be exchanged.
    try
        [retVal, flaRea, simTimRea, outputs] = exchangeDoublesWithSocket(sockfd, flaWri, length(outputs), simTimWri, inputs);

        %test socket python
        %manda todos valores climaticos para o arquivo em python

        toPython = mat2str(outputs);

        toPython = strcat(toPython, ',');
        toPython = strcat(toPython, num2str(simTimRea));


        fwrite(tcp, toPython);


        dataPython = fread(tcp, [1, tcp.BytesAvailable]);
        dataPython = str2num(char(dataPython));

        while (numel(dataPython) == 0)
            dataPython = fread(tcp, [1, tcp.BytesAvailable]);
            dataPython = str2num(char(dataPython));
        end

        %disp(dataPython);

        inputs = dataPython;
    catch ME1
        % exchangeDoublesWithSocket had an error. Terminate the connection
        disp(['Error: ', ME1.message])
        sendClientError(sockfd, -1);
        closeIPC(sockfd);
        rethrow(ME1)
    end


    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Check return flags
    if (flaRea == 1) % End of simulation
        disp('Matlab received end of simulation flag from BCVTB. Exit simulation.');
        closeIPC(sockfd);
        simulate=false;
    end

    if (retVal < 0) % Error during data exchange
        fprintf('Error: exchangeDoublesWithSocket has return value %d', retVal);
        sendClientError(sockfd, -1);
        closeIPC(sockfd);
        simulate=false;
    end

    if (flaRea > 1) % BCVTB requests termination due to an error.
        fprintf('Error: BCVTB requested termination of the simulation by sending %d\n Exit simulation.', retVal);
        sendClientError(sockfd, -1);
        closeIPC(sockfd);
        simulate=false;
    end

    if (simulate)
        simTimWri = simTimWri + delTim;
    end
end

fclose(tcp);
exit
