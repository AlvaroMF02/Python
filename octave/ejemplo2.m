% Ejemplo: Toroide Ondulado
theta = linspace(0, 2*pi, 100); % Ángulo alrededor del eje Z
phi = linspace(0, 2*pi, 100);   % Ángulo alrededor del círculo interno
[Theta, Phi] = meshgrid(theta, phi);

% Definir la forma del toroide con ondas
R = 2; % Radio principal
r = 0.5; % Radio del círculo menor
Z = (R + r .* cos(Phi) .* cos(5*Theta)) .* cos(Theta); % Coordenadas X
X = (R + r .* cos(Phi) .* cos(5*Theta)) .* sin(Theta); % Coordenadas Y
Y = r .* sin(Phi);                                    % Coordenadas Z

% Graficar el toroide ondulado
figure;
surf(X, Y, Z, 'EdgeColor', 'none'); % Superficie suave sin bordes
colormap(hot);                      % Paleta de colores cálida (hot)
shading interp;                     % Suavizar colores
colorbar;                           % Mostrar barra de colores
title('Toroide Ondulado');          % Título llamativo
xlabel('Eje X'); ylabel('Eje Y'); zlabel('Eje Z'); % Etiquetas de los ejes

% Efectos de iluminación
lighting phong;                     % Sombreado Phong
camlight headlight;                 % Luz desde la cámara
view(45, 30);                       % Ajustar el ángulo de visión
axis equal;                         % Ejes con proporciones iguales

