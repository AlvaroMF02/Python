% Ejemplo: Superficie 3D atractiva
[X, Y] = meshgrid(-3:0.1:3, -3:0.1:3); % Crear una cuadrícula de puntos
Z = sin(sqrt(X.^2 + Y.^2)) .* cos(X) .* sin(Y); % Calcular los valores de Z

% Graficar la superficie
figure;                      % Crear una nueva ventana de figura
surf(X, Y, Z, 'EdgeColor', 'none'); % Superficie suave sin bordes
colormap(jet);               % Colores atractivos (jet)
colorbar;                    % Mostrar barra de colores
title('Superficie 3D: Montaña Rusa de Funciones'); % Título
xlabel('Eje X');             % Etiqueta del eje X
ylabel('Eje Y');             % Etiqueta del eje Y
zlabel('Eje Z');             % Etiqueta del eje Z
view(45, 30);                % Ajustar la vista para un ángulo interesante

