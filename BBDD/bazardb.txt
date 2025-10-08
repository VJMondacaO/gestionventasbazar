-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 08-10-2025 a las 03:52:17
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bazardb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_app_usuario`
--

CREATE TABLE `auth_app_usuario` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `rol` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_app_usuario`
--

INSERT INTO `auth_app_usuario` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `rol`) VALUES
(1, 'pbkdf2_sha256$720000$Wwdt3BDY3dpBkMYcYfLrMD$VcQT4zPHtEKPMnscyb5CFOaTDwLFq5R/CWZOM6sEYK8=', '2025-10-08 01:43:15.149751', 0, 'vendedor1', 'Juan', 'Pérez', 'vendedor1@bazar.com', 0, 1, '2025-10-08 00:27:06.528340', 'vendedor'),
(2, 'pbkdf2_sha256$720000$rRS1g73FBiPoyOQgXPqhQ7$/GJtADMIo0w3jXLWbEcEjsHqxk6zcg+SUBFP6+pajo0=', NULL, 0, 'jefe1', 'María', 'González', 'jefe1@bazar.com', 0, 1, '2025-10-08 00:27:06.706267', 'jefe_ventas'),
(4, 'pbkdf2_sha256$720000$wriUyb5jP0aHN8d4NwqKaz$vQTmnARFipw/oGucqeNUir9AHKcG/0QXE2PKcpN7EZI=', NULL, 0, 'vendedor2', 'Elena', 'Torres', 'vendedor2@bazar.com', 0, 1, '2025-10-08 01:12:54.879522', 'vendedor'),
(5, 'pbkdf2_sha256$720000$xZ9cqyN7QlfADjKBd9Dwk5$tpFdp/jzAjLf1R1OaJmruyA8JGTiq3KZ9phLHhI7qVU=', NULL, 0, 'vendedor3', 'Claudia', 'Castillo', 'vendedor3@bazar.com', 0, 1, '2025-10-08 01:12:55.054051', 'vendedor'),
(6, 'pbkdf2_sha256$720000$1J2XPgDypDibras8TQJEJ8$r68TbCpnvUnOuhKA3xgZ8WzQOJB9++8bWYb6y2gp6EU=', NULL, 0, 'vendedor4', 'Diego', 'Torres', 'vendedor4@bazar.com', 0, 1, '2025-10-08 01:12:55.255410', 'vendedor'),
(7, 'pbkdf2_sha256$720000$NaYdx7s9j773UwzRAkjBGa$vMxiOfy4QX9Zn0AfvvpLKyh7hYKzIyaXm3L/fzP8MF0=', NULL, 0, 'vendedor5', 'Javiera', 'Martínez', 'vendedor5@bazar.com', 0, 1, '2025-10-08 01:12:55.436219', 'vendedor'),
(8, 'pbkdf2_sha256$720000$hACxT2mQo8easrbpWmbk3L$+SxTjr8a0IvMoGSNa94v8D1rBCFIxHSXr20IJHJ9jwc=', NULL, 0, 'vendedor6', 'Luis', 'Carrasco', 'vendedor6@bazar.com', 0, 1, '2025-10-08 01:12:55.606151', 'vendedor'),
(9, 'pbkdf2_sha256$720000$ylAdt7kaI7UuIcBgmEsHCe$8GG4S3RgjPJ3XLJwwZO01Dvdfb6OrL8faRpU9vAxl+U=', NULL, 0, 'vendedor7', 'Sandra', 'Hernández', 'vendedor7@bazar.com', 0, 1, '2025-10-08 01:12:55.784438', 'vendedor'),
(10, 'pbkdf2_sha256$720000$jjn5MtDk2qhOl1yXj2Pqlt$dWCcFvsDluH5iad0gVAzjfPAngkV7O3HDEXBQMXb9mk=', NULL, 0, 'vendedor8', 'Patricia', 'González', 'vendedor8@bazar.com', 0, 1, '2025-10-08 01:12:55.954798', 'vendedor'),
(11, 'pbkdf2_sha256$720000$ovwo26gkzHslfHuKyGQtd3$i/EMoKjNwz4x4aVWLFQr3pVTC/s6L+mtp4PwXUxsFnE=', NULL, 0, 'vendedor9', 'Ignacio', 'Rodríguez', 'vendedor9@bazar.com', 0, 1, '2025-10-08 01:12:56.123192', 'vendedor'),
(12, 'pbkdf2_sha256$720000$YJheQ1f1D40GTiPVwy5DXH$MV2HpTSpXGEUCWuQmes06sr6vZ+bsYeb7UGtMkGKyXs=', NULL, 0, 'vendedor10', 'Katherine', 'Jiménez', 'vendedor10@bazar.com', 0, 1, '2025-10-08 01:12:56.293555', 'vendedor'),
(13, 'pbkdf2_sha256$720000$UqUDEACvaE24PFWQiApht9$Zkm5xWQckezTNmtSV7/Cty54YnrDhJHqZA88sgh8CvA=', NULL, 0, 'vendedor11', 'Valentina', 'Jiménez', 'vendedor11@bazar.com', 0, 1, '2025-10-08 01:12:56.461950', 'vendedor'),
(14, 'pbkdf2_sha256$720000$vYfQQGlE4SFN8RgBZOnhxT$nG5hxbMvKXlUpGMcYDByWfAzfwh0b2+TQMpk3JDRPng=', NULL, 0, 'vendedor12', 'Isabel', 'Fuentes', 'vendedor12@bazar.com', 0, 1, '2025-10-08 01:12:56.630881', 'vendedor'),
(15, 'pbkdf2_sha256$720000$fRqQIFWkYlLeLZodlMuw5i$eBa4cBbmKB9sEUoYqQuoJugcP6T9NmDu5f0UOjIC3Cg=', NULL, 0, 'vendedor13', 'Gonzalo', 'Hernández', 'vendedor13@bazar.com', 0, 1, '2025-10-08 01:12:56.799244', 'vendedor'),
(16, 'pbkdf2_sha256$720000$pYm6uH5XDL9FmlztkrLEto$KIQc0Mdhj0zvZyhhDfz9ipV5GevYTK1cm7z5V5vnX0k=', NULL, 0, 'vendedor14', 'Verónica', 'Vargas', 'vendedor14@bazar.com', 0, 1, '2025-10-08 01:12:56.966619', 'vendedor'),
(17, 'pbkdf2_sha256$720000$olUNftIc4ZIbLwmaQ4XrN4$pOmRH+MF9bLKFe2XusDRtYtKPS4LrOUgY6eZR9epA6s=', NULL, 0, 'vendedor15', 'Francisco', 'Rojas', 'vendedor15@bazar.com', 0, 1, '2025-10-08 01:12:57.134288', 'vendedor'),
(18, 'pbkdf2_sha256$720000$VjjHlEwRTu1FL8HTmXK3Gk$90Hyt9rCqrrF2JC86mrFZRXbArvDuWsGud7iIvVK1K8=', NULL, 0, 'vendedor16', 'Carmen', 'Contreras', 'vendedor16@bazar.com', 0, 1, '2025-10-08 01:12:57.303595', 'vendedor'),
(19, 'pbkdf2_sha256$720000$bsLioTfDoaCGhs7QCUcU07$EPw/CGbaar8z+989pNGpcwBPiO2njpytQ8Hep6e9WBE=', NULL, 0, 'vendedor17', 'Juan', 'Muñoz', 'vendedor17@bazar.com', 0, 1, '2025-10-08 01:12:57.473131', 'vendedor'),
(20, 'pbkdf2_sha256$720000$vFRCOWzRcbVFEfUlxcqkIL$GIQcuG7P9j9PLjX5fVAGZ4qBXAm5WVbAo/peqZRANcY=', NULL, 0, 'vendedor18', 'Gonzalo', 'Gómez', 'vendedor18@bazar.com', 0, 1, '2025-10-08 01:12:57.694388', 'vendedor'),
(21, 'pbkdf2_sha256$720000$u9CnlgMsim5QkpbdMP8TXo$R7VhOJUie4LsyW/boLntzUva7PEW0USBJnk3yTcP80Y=', NULL, 0, 'vendedor19', 'José', 'Muñoz', 'vendedor19@bazar.com', 0, 1, '2025-10-08 01:12:57.868283', 'vendedor'),
(22, 'pbkdf2_sha256$720000$hkuzflIjIL0cAKmyBfvRr8$oVUcAFpeqOI6jiUORTSUDsbvEAn+XM+fm+V2lMVSXo0=', NULL, 0, 'vendedor20', 'Verónica', 'Álvarez', 'vendedor20@bazar.com', 0, 1, '2025-10-08 01:12:58.041751', 'vendedor'),
(23, 'pbkdf2_sha256$720000$5CoOuLJvHIgtnQQCalbVPp$45IdQPeRngmimsCQ5snZbcnIar5eOeBLwtmAIS0SKLw=', NULL, 0, 'jefe2', 'Fernando', 'Espinoza', 'jefe2@bazar.com', 1, 1, '2025-10-08 01:12:58.213238', 'vendedor'),
(24, 'pbkdf2_sha256$720000$jgQfg43EOxf3RkTOkn9LRj$PJ6C9+9e7lOOsAlfv9lR1zKy9mSU/jv+KMmx2qJaKKI=', NULL, 0, 'jefe3', 'Carlos', 'Tapia', 'jefe3@bazar.com', 1, 1, '2025-10-08 01:12:58.389405', 'vendedor'),
(25, 'pbkdf2_sha256$720000$0bSwsAyi0aHyZbWRcYd4zj$gRCljb0Y/2wzkCiBmkO4RXxpawaqIw9KU0zIsEGtod8=', NULL, 0, 'jefe4', 'Paula', 'Fernández', 'jefe4@bazar.com', 1, 1, '2025-10-08 01:12:58.568612', 'vendedor'),
(26, 'pbkdf2_sha256$720000$YvxpBuUA0mnmifhFXn2aRV$qc54InLGrkt6yuXWn8GEasveDpN3C5/7QhgXC9kiOts=', NULL, 0, 'jefe5', 'Diego', 'Fernández', 'jefe5@bazar.com', 1, 1, '2025-10-08 01:12:58.737360', 'vendedor'),
(27, 'pbkdf2_sha256$720000$fzGV89KZ7Hq3BvhKT15rqt$aMlo2+suKEwF1hoCtz8dQcVM2YPi90JgaYtOvMc2Y6A=', NULL, 0, 'vendedor21', 'María', 'González', 'maria@bazar.com', 0, 1, '2025-10-08 01:14:38.506618', 'vendedor'),
(28, 'pbkdf2_sha256$720000$nBbBhlkmNeFUs4g1hgAGnt$TCUlcFY2Vp2FK9g9kybmExMw98prx+bYI+Zhz38KT0A=', NULL, 0, 'vendedor22', 'Carlos', 'López', 'carlos@bazar.com', 0, 1, '2025-10-08 01:14:38.708553', 'vendedor'),
(29, 'pbkdf2_sha256$720000$DTKOsuYq8wdDYKVpfXyr4Q$3ogB1uya6qZ076TUGVAdmlJgOBo9dQu2Lt61z7brRbM=', NULL, 0, 'vendedor23', 'Ana', 'Martín', 'ana@bazar.com', 0, 1, '2025-10-08 01:14:38.895040', 'vendedor'),
(30, 'pbkdf2_sha256$720000$W6kgjnYA35sXGU6561tan1$YdBCnBelHX2Ylo1OtyfYcgjtFdAQEgR75TY/7WUusMQ=', NULL, 0, 'vendedor24', 'Luis', 'Sánchez', 'luis@bazar.com', 0, 1, '2025-10-08 01:14:39.077691', 'vendedor'),
(31, 'pbkdf2_sha256$720000$QRF5lEjt1cGVROj4SEYrZ6$QbWwjEfFQQNWXSRlrRSm/npNG6j6SQ/e/3I5FSQWbtI=', NULL, 0, 'vendedor25', 'Carmen', 'Pérez', 'carmen@bazar.com', 0, 1, '2025-10-08 01:14:39.254968', 'vendedor'),
(32, 'pbkdf2_sha256$720000$FkV60gHTROUqN0WXWDSCde$00KfSHQJ8jwQFKMFvfDsoY/sZooR02GKear/PuQMews=', NULL, 0, 'vendedor26', 'Vendedor26', 'Apellido', 'vendedor26@bazar.com', 0, 1, '2025-10-08 01:15:08.812645', 'vendedor'),
(33, 'pbkdf2_sha256$720000$LLUQBXXss1w5V1v4rtqtwC$/GY7LJGp1Gy6S9PPdVdF1KUS7wUfGVtVKnet6Uv/ko8=', NULL, 0, 'vendedor27', 'Vendedor27', 'Apellido', 'vendedor27@bazar.com', 0, 1, '2025-10-08 01:15:09.005088', 'vendedor'),
(34, 'pbkdf2_sha256$720000$7W8OXAKw9UiYsB08bppoAG$58HNCTMf9MPvIfo5hAFZJ9gG4qY1cf/ODSiQ77zPAZ4=', NULL, 0, 'vendedor28', 'Vendedor28', 'Apellido', 'vendedor28@bazar.com', 0, 1, '2025-10-08 01:15:09.175603', 'vendedor'),
(35, 'pbkdf2_sha256$720000$QJOMvL5FjAB1kJe3lEyens$r9ZEy0e80MgncDFAVcyt+oDhza/Gb0cqitKESCGIP2s=', NULL, 0, 'vendedor29', 'Vendedor29', 'Apellido', 'vendedor29@bazar.com', 0, 1, '2025-10-08 01:15:09.346581', 'vendedor'),
(36, 'pbkdf2_sha256$720000$XkmuXlRvNYAV6M5xrwsNc4$n2o6eyJbCEnP7ROVW2vLlfmJkKhgIrAKSa4BRbDMsLc=', NULL, 0, 'vendedor30', 'Vendedor30', 'Apellido', 'vendedor30@bazar.com', 0, 1, '2025-10-08 01:15:09.515522', 'vendedor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_app_usuario_groups`
--

CREATE TABLE `auth_app_usuario_groups` (
  `id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_app_usuario_user_permissions`
--

CREATE TABLE `auth_app_usuario_user_permissions` (
  `id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_usuario'),
(22, 'Can change user', 6, 'change_usuario'),
(23, 'Can delete user', 6, 'delete_usuario'),
(24, 'Can view user', 6, 'view_usuario'),
(25, 'Can add Venta', 7, 'add_venta'),
(26, 'Can change Venta', 7, 'change_venta'),
(27, 'Can delete Venta', 7, 'delete_venta'),
(28, 'Can view Venta', 7, 'view_venta'),
(29, 'Can add Item de Venta', 8, 'add_itemventa'),
(30, 'Can change Item de Venta', 8, 'change_itemventa'),
(31, 'Can delete Item de Venta', 8, 'delete_itemventa'),
(32, 'Can view Item de Venta', 8, 'view_itemventa'),
(33, 'Can add Resumen Diario', 9, 'add_resumendiario'),
(34, 'Can change Resumen Diario', 9, 'change_resumendiario'),
(35, 'Can delete Resumen Diario', 9, 'delete_resumendiario'),
(36, 'Can view Resumen Diario', 9, 'view_resumendiario'),
(37, 'Can add clientes', 10, 'add_clientes'),
(38, 'Can change clientes', 10, 'change_clientes'),
(39, 'Can delete clientes', 10, 'delete_clientes'),
(40, 'Can view clientes', 10, 'view_clientes'),
(41, 'Can add productos', 11, 'add_productos'),
(42, 'Can change productos', 11, 'change_productos'),
(43, 'Can delete productos', 11, 'delete_productos'),
(44, 'Can view productos', 11, 'view_productos'),
(45, 'Can add Control de Día', 12, 'add_controldia'),
(46, 'Can change Control de Día', 12, 'change_controldia'),
(47, 'Can delete Control de Día', 12, 'delete_controldia'),
(48, 'Can view Control de Día', 12, 'view_controldia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `djangoVerVictorMondaca_clientes`
--

CREATE TABLE `djangoVerVictorMondaca_clientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `comuna` varchar(50) NOT NULL,
  `region` varchar(50) NOT NULL,
  `fecha_registro` date NOT NULL,
  `tipo_cliente` varchar(20) NOT NULL,
  `observaciones` longtext DEFAULT NULL,
  `rut` varchar(12) NOT NULL,
  `tipo_persona` varchar(20) NOT NULL,
  `giro` varchar(100) DEFAULT NULL,
  `contacto` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `djangoVerVictorMondaca_clientes`
--

INSERT INTO `djangoVerVictorMondaca_clientes` (`id`, `nombre`, `email`, `telefono`, `direccion`, `comuna`, `region`, `fecha_registro`, `tipo_cliente`, `observaciones`, `rut`, `tipo_persona`, `giro`, `contacto`) VALUES
(1, 'Ana García Silva', 'ana.garcia@email.com', '+56 9 1234 5678', 'Av. Libertador Bernardo O\'Higgins 123', 'Santiago', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '12.345.678-9', 'natural', NULL, NULL),
(2, 'Carlos López Pérez', 'carlos.lopez@email.com', '+56 9 8765 4321', 'Calle Las Flores 456', 'Providencia', 'Metropolitana', '2025-10-07', 'contribuyente', NULL, '98.765.432-1', 'natural', NULL, NULL),
(3, 'Restaurante El Buen Sabor', 'contacto@buensabor.cl', '+56 2 2345 6789', 'Av. Providencia 789', 'Providencia', 'Metropolitana', '2025-10-07', 'empresa', NULL, '76.543.210-K', 'juridica', 'Restaurante', 'María Rodríguez'),
(4, 'Pedro Martínez González', 'pedro.martinez@email.com', '+56 9 3456 7890', 'Pasaje Los Robles 321', 'Las Condes', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '11.222.333-4', 'natural', NULL, NULL),
(5, 'Carmen Cortés', 'carmen.cortés@email.com', '+56947238922', 'Av. Constitución #6317', 'La Serena', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '8.811.673-9', 'natural', NULL, NULL),
(6, 'Paula Díaz', 'paula.díaz@email.com', '+56918709064', 'Calle República #8648', 'Antofagasta', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '18.337.074-K', 'natural', NULL, NULL),
(7, 'Fernando Núñez', 'fernando.núñez@email.com', '+56917068848', 'Pasaje Libertador #6311', 'Coquimbo', 'Maule', '2025-10-07', 'Empresa', NULL, '21.167.345-1', 'natural', NULL, NULL),
(8, 'Valentina Moreno', 'valentina.moreno@email.com', '+56994387138', 'Pasaje Libertador #6037', 'Puente Alto', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '21.696.466-7', 'natural', NULL, NULL),
(9, 'Fernando Gómez', 'fernando.gómez@email.com', '+56954466864', 'Calle Constitución #2432', 'Concepción', 'Coquimbo', '2025-10-07', 'Contribuyente', NULL, '15.126.135-3', 'natural', NULL, NULL),
(10, 'Valentina Muñoz', 'valentina.muñoz@email.com', '+56942797972', 'Av. Libertador #3966', 'Iquique', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '13.805.171-4', 'natural', NULL, NULL),
(11, 'Manuel Sepúlveda', 'manuel.sepúlveda@email.com', '+56944468311', 'Av. Constitución #4090', 'Punta Arenas', 'Maule', '2025-10-07', 'Contribuyente', NULL, '23.532.251-K', 'natural', NULL, NULL),
(12, 'Carlos Gutiérrez', 'carlos.gutiérrez@email.com', '+56951496249', 'Calle República #5516', 'Iquique', 'Magallanes', '2025-10-07', 'Empresa', NULL, '18.659.523-8', 'natural', NULL, NULL),
(13, 'Natalia Reyes', 'natalia.reyes@email.com', '+56928538695', 'Pasaje Libertador #4300', 'Coquimbo', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '21.142.575-K', 'natural', NULL, NULL),
(14, 'Rosa Fernández', 'rosa.fernández@email.com', '+56963301343', 'Calle República #7328', 'Coquimbo', 'Arica y Parinacota', '2025-10-07', 'Empresa', NULL, '4.084.096-6', 'natural', NULL, NULL),
(15, 'Diego González', 'diego.gonzález@email.com', '+56941459051', 'Av. Constitución #2054', 'Osorno', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '15.834.248-0', 'natural', NULL, NULL),
(16, 'Manuel Araya', 'manuel.araya@email.com', '+56915557528', 'Pasaje Constitución #4689', 'Rancagua', 'Maule', '2025-10-07', 'Contribuyente', NULL, '9.333.097-8', 'natural', NULL, NULL),
(17, 'Isabel Parra', 'isabel.parra@email.com', '+56952981114', 'Av. Constitución #1273', 'Valparaíso', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '11.160.860-1', 'natural', NULL, NULL),
(18, 'Diego Araya', 'diego.araya@email.com', '+56929245595', 'Pasaje Libertador #4428', 'Ñuñoa', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '18.489.919-1', 'natural', NULL, NULL),
(19, 'Gabriel Jiménez', 'gabriel.jiménez@email.com', '+56945465695', 'Av. Constitución #8812', 'Viña del Mar', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '22.709.782-5', 'natural', NULL, NULL),
(20, 'Francisca Parra', 'francisca.parra@email.com', '+56967647743', 'Av. Constitución #3354', 'Maipú', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '20.426.846-0', 'natural', NULL, NULL),
(21, 'Rosa Araya', 'rosa.araya@email.com', '+56991012406', 'Calle Libertador #1996', 'Ñuñoa', 'Arica y Parinacota', '2025-10-07', 'Empresa', NULL, '19.439.517-5', 'natural', NULL, NULL),
(22, 'Javiera Tapia', 'javiera.tapia@email.com', '+56918756274', 'Calle Libertador #6421', 'Las Condes', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '20.567.251-6', 'natural', NULL, NULL),
(23, 'Sofía Flores', 'sofía.flores@email.com', '+56936765148', 'Pasaje República #5673', 'Providencia', 'Ñuble', '2025-10-07', 'Empresa', NULL, '10.082.089-7', 'natural', NULL, NULL),
(24, 'Francisco Gutiérrez', 'francisco.gutiérrez@email.com', '+56942194857', 'Pasaje Libertador #3016', 'Concepción', 'Metropolitana', '2025-10-07', 'Consumidor Final', NULL, '6.415.626-8', 'natural', NULL, NULL),
(25, 'Carmen Sánchez', 'carmen.sánchez@email.com', '+56992721907', 'Av. Independencia #9791', 'Las Condes', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '9.876.841-6', 'natural', NULL, NULL),
(26, 'Elena Jiménez', 'elena.jiménez@email.com', '+56997535410', 'Pasaje Independencia #9901', 'Osorno', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '18.832.726-5', 'natural', NULL, NULL),
(27, 'Manuel Contreras', 'manuel.contreras@email.com', '+56945629793', 'Calle Independencia #6346', 'Puerto Montt', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '18.291.708-7', 'natural', NULL, NULL),
(28, 'Jorge Valenzuela', 'jorge.valenzuela@email.com', '+56933407182', 'Pasaje Libertador #5427', 'Maipú', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '18.371.472-4', 'natural', NULL, NULL),
(29, 'Ana Soto', 'ana.soto@email.com', '+56923448124', 'Pasaje Constitución #7022', 'Valparaíso', 'Ñuble', '2025-10-07', 'Consumidor Final', NULL, '2.879.907-1', 'natural', NULL, NULL),
(30, 'Diego Rojas', 'diego.rojas@email.com', '+56946661415', 'Av. Constitución #430', 'Viña del Mar', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '20.475.605-8', 'natural', NULL, NULL),
(31, 'Paula Flores', 'paula.flores@email.com', '+56913556506', 'Av. Independencia #7251', 'Puerto Montt', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '8.161.474-1', 'natural', NULL, NULL),
(32, 'Natalia Martínez', 'natalia.martínez@email.com', '+56961691812', 'Pasaje Constitución #4228', 'Maipú', 'Los Lagos', '2025-10-07', 'Contribuyente', NULL, '10.640.018-0', 'natural', NULL, NULL),
(33, 'Laura Vásquez', 'laura.vásquez@email.com', '+56981442434', 'Calle Libertador #2549', 'Arica', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '11.841.821-2', 'natural', NULL, NULL),
(34, 'Gonzalo Gutiérrez', 'gonzalo.gutiérrez@email.com', '+56958900193', 'Calle Libertador #6642', 'Rancagua', 'Magallanes', '2025-10-07', 'Empresa', NULL, '2.625.318-7', 'natural', NULL, NULL),
(35, 'Verónica González', 'verónica.gonzález@email.com', '+56979476179', 'Calle Libertador #9072', 'Puente Alto', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '23.552.296-9', 'natural', NULL, NULL),
(36, 'Cristian Araya', 'cristian.araya@email.com', '+56958042520', 'Calle Libertador #9618', 'Osorno', 'Valparaíso', '2025-10-07', 'Consumidor Final', NULL, '13.441.347-6', 'natural', NULL, NULL),
(37, 'Manuel Araya', 'manuel.araya@email.com', '+56910510631', 'Calle República #521', 'Las Condes', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '20.952.429-5', 'natural', NULL, NULL),
(38, 'Valentina Parra', 'valentina.parra@email.com', '+56990323686', 'Av. República #6390', 'Valparaíso', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '5.887.033-1', 'natural', NULL, NULL),
(39, 'Cristian Parra', 'cristian.parra@email.com', '+56936195438', 'Pasaje Constitución #4426', 'Antofagasta', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '19.929.748-1', 'natural', NULL, NULL),
(40, 'Juan Contreras', 'juan.contreras@email.com', '+56925863636', 'Pasaje Libertador #7457', 'La Florida', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '9.743.350-K', 'natural', NULL, NULL),
(41, 'María Núñez', 'maría.núñez@email.com', '+56927052600', 'Pasaje República #9797', 'Puerto Montt', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '9.990.283-3', 'natural', NULL, NULL),
(42, 'Gabriel Rodríguez', 'gabriel.rodríguez@email.com', '+56921349269', 'Av. Libertador #3761', 'Talca', 'Biobío', '2025-10-07', 'Empresa', NULL, '22.873.792-5', 'natural', NULL, NULL),
(43, 'Natalia Fuentes', 'natalia.fuentes@email.com', '+56980799391', 'Pasaje Independencia #9730', 'Rancagua', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '20.759.894-1', 'natural', NULL, NULL),
(44, 'Diego Soto', 'diego.soto@email.com', '+56980482663', 'Pasaje República #1005', 'Puente Alto', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '2.611.336-9', 'natural', NULL, NULL),
(45, 'Eduardo Rojas', 'eduardo.rojas@email.com', '+56980696737', 'Pasaje República #6947', 'Antofagasta', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '4.496.931-9', 'natural', NULL, NULL),
(46, 'Andrés Espinoza', 'andrés.espinoza@email.com', '+56955462924', 'Pasaje Constitución #984', 'Rancagua', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '9.176.661-2', 'natural', NULL, NULL),
(47, 'Katherine Morales', 'katherine.morales@email.com', '+56949626555', 'Pasaje Independencia #6612', 'Iquique', 'Magallanes', '2025-10-07', 'Empresa', NULL, '8.208.169-0', 'natural', NULL, NULL),
(48, 'Patricia Carrasco', 'patricia.carrasco@email.com', '+56952326628', 'Calle Constitución #9146', 'San Bernardo', 'Maule', '2025-10-07', 'Empresa', NULL, '1.186.498-8', 'natural', NULL, NULL),
(49, 'Francisca Parra', 'francisca.parra@email.com', '+56927465167', 'Av. Independencia #9875', 'Iquique', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '9.957.351-1', 'natural', NULL, NULL),
(50, 'Patricia Castro', 'patricia.castro@email.com', '+56981175614', 'Calle Independencia #806', 'Valparaíso', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '1.932.960-7', 'natural', NULL, NULL),
(51, 'Patricia Vásquez', 'patricia.vásquez@email.com', '+56951675570', 'Av. Constitución #9813', 'San Bernardo', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '16.961.147-5', 'natural', NULL, NULL),
(52, 'Laura Castro', 'laura.castro@email.com', '+56914214008', 'Pasaje República #1591', 'Chillán', 'Maule', '2025-10-07', 'Contribuyente', NULL, '19.936.178-3', 'natural', NULL, NULL),
(53, 'Marcela Hernández', 'marcela.hernández@email.com', '+56924357561', 'Calle Libertador #5479', 'Temuco', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '12.903.104-2', 'natural', NULL, NULL),
(54, 'Héctor Flores', 'héctor.flores@email.com', '+56921732946', 'Calle República #956', 'Arica', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '12.282.789-5', 'natural', NULL, NULL),
(55, 'Sandra Castro', 'sandra.castro@email.com', '+56988751027', 'Pasaje Independencia #7307', 'Ñuñoa', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '14.880.514-8', 'natural', NULL, NULL),
(56, 'Lorena López', 'lorena.lópez@email.com', '+56930702135', 'Calle República #1746', 'La Serena', 'Ñuble', '2025-10-07', 'Consumidor Final', NULL, '22.950.121-6', 'natural', NULL, NULL),
(57, 'Gonzalo Soto', 'gonzalo.soto@email.com', '+56939398808', 'Calle Independencia #8608', 'Antofagasta', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '9.015.445-1', 'natural', NULL, NULL),
(58, 'Marcela Álvarez', 'marcela.álvarez@email.com', '+56939368802', 'Av. Libertador #6680', 'La Florida', 'Ñuble', '2025-10-07', 'Empresa', NULL, '8.418.559-0', 'natural', NULL, NULL),
(59, 'Valentina Herrera', 'valentina.herrera@email.com', '+56932933792', 'Av. Constitución #6740', 'Punta Arenas', 'Ñuble', '2025-10-07', 'Empresa', NULL, '23.291.629-K', 'natural', NULL, NULL),
(60, 'Verónica Herrera', 'verónica.herrera@email.com', '+56974668773', 'Calle Libertador #8071', 'La Florida', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '10.987.150-8', 'natural', NULL, NULL),
(61, 'Sofía Flores', 'sofía.flores@email.com', '+56932146594', 'Pasaje Constitución #3973', 'Iquique', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '18.452.073-7', 'natural', NULL, NULL),
(62, 'Natalia Sepúlveda', 'natalia.sepúlveda@email.com', '+56976685783', 'Pasaje República #3050', 'Concepción', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '9.561.887-1', 'natural', NULL, NULL),
(63, 'Marcela Cortés', 'marcela.cortés@email.com', '+56923342157', 'Pasaje República #2624', 'Providencia', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '2.357.152-8', 'natural', NULL, NULL),
(64, 'Patricia Morales', 'patricia.morales@email.com', '+56987224316', 'Pasaje Constitución #9665', 'Maipú', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '16.930.944-2', 'natural', NULL, NULL),
(65, 'Paula Tapia', 'paula.tapia@email.com', '+56915505590', 'Av. Libertador #3775', 'Providencia', 'Biobío', '2025-10-07', 'Empresa', NULL, '5.653.569-1', 'natural', NULL, NULL),
(66, 'Daniel Castro', 'daniel.castro@email.com', '+56954809957', 'Av. República #6790', 'Las Condes', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '10.057.744-5', 'natural', NULL, NULL),
(67, 'Manuel Contreras', 'manuel.contreras@email.com', '+56932029728', 'Pasaje Libertador #1493', 'Las Condes', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '7.435.974-4', 'natural', NULL, NULL),
(68, 'Javiera Espinoza', 'javiera.espinoza@email.com', '+56976295306', 'Pasaje Libertador #4226', 'Talca', 'Maule', '2025-10-07', 'Empresa', NULL, '5.478.773-1', 'natural', NULL, NULL),
(69, 'José Muñoz', 'josé.muñoz@email.com', '+56998242522', 'Av. Libertador #445', 'Concepción', 'Biobío', '2025-10-07', 'Empresa', NULL, '13.155.857-0', 'natural', NULL, NULL),
(70, 'Manuel Rodríguez', 'manuel.rodríguez@email.com', '+56975374731', 'Calle Libertador #4786', 'Las Condes', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '11.489.464-8', 'natural', NULL, NULL),
(71, 'Katherine Tapia', 'katherine.tapia@email.com', '+56915708887', 'Calle Libertador #1213', 'Iquique', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '6.033.719-5', 'natural', NULL, NULL),
(72, 'Javier Herrera', 'javier.herrera@email.com', '+56939237082', 'Calle Libertador #7478', 'Arica', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '5.760.678-9', 'natural', NULL, NULL),
(73, 'Elena Parra', 'elena.parra@email.com', '+56995982136', 'Calle Libertador #9302', 'Santiago', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '10.885.700-5', 'natural', NULL, NULL),
(74, 'Jorge Cortés', 'jorge.cortés@email.com', '+56935970887', 'Av. Constitución #3576', 'Santiago', 'Biobío', '2025-10-07', 'Empresa', NULL, '18.724.877-9', 'natural', NULL, NULL),
(75, 'Manuel Tapia', 'manuel.tapia@email.com', '+56963245805', 'Av. Independencia #3478', 'Santiago', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '11.203.820-5', 'natural', NULL, NULL),
(76, 'José Rodríguez', 'josé.rodríguez@email.com', '+56971969450', 'Pasaje República #2585', 'Providencia', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '9.379.224-6', 'natural', NULL, NULL),
(77, 'Marcela Contreras', 'marcela.contreras@email.com', '+56917452890', 'Av. Constitución #9424', 'Chillán', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '15.721.671-6', 'natural', NULL, NULL),
(78, 'Sandra Moreno', 'sandra.moreno@email.com', '+56997607374', 'Av. Constitución #7781', 'Las Condes', 'Coquimbo', '2025-10-07', 'Contribuyente', NULL, '21.819.907-0', 'natural', NULL, NULL),
(79, 'Katherine Álvarez', 'katherine.álvarez@email.com', '+56995699077', 'Calle Libertador #2922', 'Valparaíso', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '23.523.371-1', 'natural', NULL, NULL),
(80, 'Gabriel Sepúlveda', 'gabriel.sepúlveda@email.com', '+56928923255', 'Av. República #5466', 'Arica', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '22.775.360-9', 'natural', NULL, NULL),
(81, 'Diego Díaz', 'diego.díaz@email.com', '+56927729259', 'Pasaje Libertador #325', 'Coquimbo', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '5.901.005-0', 'natural', NULL, NULL),
(82, 'Diego Valenzuela', 'diego.valenzuela@email.com', '+56983389037', 'Calle Libertador #7264', 'Osorno', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '22.672.321-8', 'natural', NULL, NULL),
(83, 'Héctor Ramírez', 'héctor.ramírez@email.com', '+56941343684', 'Calle Independencia #9377', 'Concepción', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '12.811.486-6', 'natural', NULL, NULL),
(84, 'Rosa Pérez', 'rosa.pérez@email.com', '+56984273936', 'Av. República #7635', 'Viña del Mar', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '14.843.984-2', 'natural', NULL, NULL),
(85, 'Patricia Vera', 'patricia.vera@email.com', '+56943993707', 'Av. Independencia #2170', 'Coquimbo', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '21.494.535-5', 'natural', NULL, NULL),
(86, 'Juan González', 'juan.gonzález@email.com', '+56963178372', 'Av. Independencia #7265', 'La Serena', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '12.038.322-1', 'natural', NULL, NULL),
(87, 'Paula Fuentes', 'paula.fuentes@email.com', '+56991979009', 'Pasaje Libertador #1352', 'Osorno', 'Magallanes', '2025-10-07', 'Empresa', NULL, '10.988.510-K', 'natural', NULL, NULL),
(88, 'Juan Rojas', 'juan.rojas@email.com', '+56966158395', 'Av. Independencia #5714', 'Santiago', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '10.264.586-3', 'natural', NULL, NULL),
(89, 'Lorena Reyes', 'lorena.reyes@email.com', '+56989287174', 'Av. Constitución #3682', 'Punta Arenas', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '23.806.987-4', 'natural', NULL, NULL),
(90, 'Claudia Sepúlveda', 'claudia.sepúlveda@email.com', '+56993282567', 'Calle Independencia #7591', 'Puente Alto', 'Maule', '2025-10-07', 'Contribuyente', NULL, '18.606.723-1', 'natural', NULL, NULL),
(91, 'Sofía Reyes', 'sofía.reyes@email.com', '+56969765965', 'Calle Independencia #9050', 'Providencia', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '7.995.144-7', 'natural', NULL, NULL),
(92, 'Carmen Tapia', 'carmen.tapia@email.com', '+56960035053', 'Calle Independencia #7703', 'Ñuñoa', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '6.854.415-7', 'natural', NULL, NULL),
(93, 'Diego Parra', 'diego.parra@email.com', '+56982582348', 'Pasaje Independencia #6535', 'Rancagua', 'Coquimbo', '2025-10-07', 'Empresa', NULL, '9.530.865-1', 'natural', NULL, NULL),
(94, 'Héctor Cortés', 'héctor.cortés@email.com', '+56932372888', 'Pasaje Constitución #2892', 'Talca', 'Magallanes', '2025-10-07', 'Empresa', NULL, '16.338.084-6', 'natural', NULL, NULL),
(95, 'Verónica Reyes', 'verónica.reyes@email.com', '+56960384222', 'Pasaje Libertador #2960', 'Concepción', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '24.745.137-4', 'natural', NULL, NULL),
(96, 'Francisco Flores', 'francisco.flores@email.com', '+56930843587', 'Pasaje Independencia #6871', 'Coquimbo', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '13.165.151-1', 'natural', NULL, NULL),
(97, 'Ana Pérez', 'ana.pérez@email.com', '+56964124713', 'Pasaje Libertador #368', 'San Bernardo', 'Coquimbo', '2025-10-07', 'Empresa', NULL, '13.572.622-2', 'natural', NULL, NULL),
(98, 'Isabel Espinoza', 'isabel.espinoza@email.com', '+56994988830', 'Calle Libertador #7725', 'Talca', 'Valparaíso', '2025-10-07', 'Consumidor Final', NULL, '9.485.388-5', 'natural', NULL, NULL),
(99, 'Paula Fernández', 'paula.fernández@email.com', '+56971436424', 'Calle Constitución #3002', 'Punta Arenas', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '3.179.298-3', 'natural', NULL, NULL),
(100, 'Héctor Cortés', 'héctor.cortés@email.com', '+56965308576', 'Pasaje Independencia #7046', 'Coquimbo', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '21.099.719-9', 'natural', NULL, NULL),
(101, 'Isabel Pérez', 'isabel.pérez@email.com', '+56953118565', 'Calle República #6961', 'Puerto Montt', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '7.798.027-K', 'natural', NULL, NULL),
(102, 'Fernando Núñez', 'fernando.núñez@email.com', '+56984904675', 'Av. Constitución #3800', 'Santiago', 'Ñuble', '2025-10-07', 'Empresa', NULL, '11.005.330-4', 'natural', NULL, NULL),
(103, 'Laura Sánchez', 'laura.sánchez@email.com', '+56999778185', 'Calle Libertador #8446', 'Temuco', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '12.613.672-2', 'natural', NULL, NULL),
(104, 'Jorge Sepúlveda', 'jorge.sepúlveda@email.com', '+56978003731', 'Calle Independencia #5765', 'Puente Alto', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '8.446.139-3', 'natural', NULL, NULL),
(105, 'Francisco Ramírez', 'francisco.ramírez@email.com', '+56954455439', 'Calle Constitución #999', 'Temuco', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '1.500.579-3', 'natural', NULL, NULL),
(106, 'Lorena Vásquez', 'lorena.vásquez@email.com', '+56918901536', 'Pasaje Constitución #9072', 'La Serena', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '19.746.640-5', 'natural', NULL, NULL),
(107, 'Alejandro Cortés', 'alejandro.cortés@email.com', '+56923030060', 'Pasaje República #9166', 'San Bernardo', 'Maule', '2025-10-07', 'Empresa', NULL, '19.826.776-7', 'natural', NULL, NULL),
(108, 'Fernando Hernández', 'fernando.hernández@email.com', '+56944004474', 'Av. República #5164', 'Talca', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '16.032.353-1', 'natural', NULL, NULL),
(109, 'Patricia Valenzuela', 'patricia.valenzuela@email.com', '+56959123082', 'Calle República #3337', 'Temuco', 'Valparaíso', '2025-10-07', 'Consumidor Final', NULL, '11.152.822-5', 'natural', NULL, NULL),
(110, 'Carmen Fernández', 'carmen.fernández@email.com', '+56921903588', 'Calle Libertador #4112', 'Arica', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '16.058.383-5', 'natural', NULL, NULL),
(111, 'Luis Pérez', 'luis.pérez@email.com', '+56934176087', 'Calle Constitución #1870', 'La Serena', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '13.782.071-4', 'natural', NULL, NULL),
(112, 'Paula López', 'paula.lópez@email.com', '+56923627718', 'Calle Constitución #169', 'Santiago', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '6.547.424-7', 'natural', NULL, NULL),
(113, 'Fernando Vargas', 'fernando.vargas@email.com', '+56932920323', 'Pasaje Independencia #7622', 'San Bernardo', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '14.996.272-7', 'natural', NULL, NULL),
(114, 'Javiera Pérez', 'javiera.pérez@email.com', '+56985684170', 'Pasaje Independencia #2130', 'Punta Arenas', 'Ñuble', '2025-10-07', 'Consumidor Final', NULL, '11.426.557-8', 'natural', NULL, NULL),
(115, 'Andrés Ramírez', 'andrés.ramírez@email.com', '+56926540286', 'Av. República #6092', 'La Serena', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '17.042.824-2', 'natural', NULL, NULL),
(116, 'Patricia Castillo', 'patricia.castillo@email.com', '+56940584269', 'Av. República #7613', 'Talca', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '4.188.744-3', 'natural', NULL, NULL),
(117, 'Elena Vásquez', 'elena.vásquez@email.com', '+56946682736', 'Av. Constitución #3279', 'Ñuñoa', 'Ñuble', '2025-10-07', 'Empresa', NULL, '2.128.565-K', 'natural', NULL, NULL),
(118, 'Andrés Vera', 'andrés.vera@email.com', '+56952305646', 'Pasaje República #7602', 'Concepción', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '8.842.579-0', 'natural', NULL, NULL),
(119, 'Fernando Castro', 'fernando.castro@email.com', '+56977833008', 'Calle Independencia #2582', 'Santiago', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '9.750.189-0', 'natural', NULL, NULL),
(120, 'Valentina Fuentes', 'valentina.fuentes@email.com', '+56996249318', 'Calle Libertador #1164', 'Punta Arenas', 'Arica y Parinacota', '2025-10-07', 'Empresa', NULL, '17.766.299-2', 'natural', NULL, NULL),
(121, 'Gonzalo Núñez', 'gonzalo.núñez@email.com', '+56976938050', 'Calle Libertador #4831', 'Osorno', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '7.835.273-6', 'natural', NULL, NULL),
(122, 'Patricia Valenzuela', 'patricia.valenzuela@email.com', '+56933292329', 'Calle Libertador #4600', 'Viña del Mar', 'Coquimbo', '2025-10-07', 'Contribuyente', NULL, '12.303.457-0', 'natural', NULL, NULL),
(123, 'Rosa Gómez', 'rosa.gómez@email.com', '+56910723671', 'Pasaje Libertador #6412', 'La Florida', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '22.590.463-4', 'natural', NULL, NULL),
(124, 'Paula Fernández', 'paula.fernández@email.com', '+56982402817', 'Av. Constitución #4810', 'Iquique', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '15.752.978-1', 'natural', NULL, NULL),
(125, 'Luis Martínez', 'luis.martínez@email.com', '+56952170320', 'Pasaje Libertador #8196', 'Temuco', 'Magallanes', '2025-10-07', 'Empresa', NULL, '9.464.839-4', 'natural', NULL, NULL),
(126, 'Carmen Espinoza', 'carmen.espinoza@email.com', '+56910232516', 'Calle Independencia #5705', 'Rancagua', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '4.246.129-6', 'natural', NULL, NULL),
(127, 'Héctor Tapia', 'héctor.tapia@email.com', '+56954117968', 'Av. República #728', 'San Bernardo', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '3.467.063-3', 'natural', NULL, NULL),
(128, 'Jorge Cortés', 'jorge.cortés@email.com', '+56934531959', 'Calle Constitución #7404', 'Santiago', 'Arica y Parinacota', '2025-10-07', 'Empresa', NULL, '19.948.451-6', 'natural', NULL, NULL),
(129, 'Laura Jiménez', 'laura.jiménez@email.com', '+56935900027', 'Calle Independencia #6785', 'Temuco', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '16.574.271-0', 'natural', NULL, NULL),
(130, 'Rosa Cortés', 'rosa.cortés@email.com', '+56999477048', 'Av. República #4569', 'Punta Arenas', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '20.959.683-0', 'natural', NULL, NULL),
(131, 'Carlos Flores', 'carlos.flores@email.com', '+56915418620', 'Calle Libertador #5061', 'Arica', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '3.629.301-2', 'natural', NULL, NULL),
(132, 'Francisco Gómez', 'francisco.gómez@email.com', '+56946970521', 'Av. Libertador #8017', 'Osorno', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '2.100.520-7', 'natural', NULL, NULL),
(133, 'Laura Soto', 'laura.soto@email.com', '+56912743426', 'Calle Independencia #4114', 'Concepción', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '8.982.026-K', 'natural', NULL, NULL),
(134, 'Rosa Jiménez', 'rosa.jiménez@email.com', '+56988067918', 'Av. Independencia #8968', 'Temuco', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '14.622.797-K', 'natural', NULL, NULL),
(135, 'Cristian Díaz', 'cristian.díaz@email.com', '+56930636911', 'Calle Independencia #5346', 'La Serena', 'Maule', '2025-10-07', 'Empresa', NULL, '8.863.166-8', 'natural', NULL, NULL),
(136, 'María Fuentes', 'maría.fuentes@email.com', '+56988468901', 'Pasaje Libertador #420', 'Puerto Montt', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '16.600.888-3', 'natural', NULL, NULL),
(137, 'Isabel Morales', 'isabel.morales@email.com', '+56921238401', 'Calle Constitución #9997', 'Puente Alto', 'Biobío', '2025-10-07', 'Empresa', NULL, '16.718.878-8', 'natural', NULL, NULL),
(138, 'Javiera Espinoza', 'javiera.espinoza@email.com', '+56972767341', 'Av. Libertador #487', 'Antofagasta', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '22.179.654-3', 'natural', NULL, NULL),
(139, 'Daniel Martínez', 'daniel.martínez@email.com', '+56985990306', 'Av. Libertador #4332', 'Maipú', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '14.954.428-3', 'natural', NULL, NULL),
(140, 'Manuel Parra', 'manuel.parra@email.com', '+56974674530', 'Av. República #8407', 'Viña del Mar', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '17.289.979-K', 'natural', NULL, NULL),
(141, 'José Herrera', 'josé.herrera@email.com', '+56997833335', 'Calle República #6700', 'San Bernardo', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '4.334.005-0', 'natural', NULL, NULL),
(142, 'Katherine Vera', 'katherine.vera@email.com', '+56995058540', 'Calle Independencia #2032', 'La Serena', 'Arica y Parinacota', '2025-10-07', 'Empresa', NULL, '7.258.832-0', 'natural', NULL, NULL),
(143, 'Antonio Martínez', 'antonio.martínez@email.com', '+56956474659', 'Av. Constitución #6724', 'Santiago', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '19.256.589-8', 'natural', NULL, NULL),
(144, 'Diego Vásquez', 'diego.vásquez@email.com', '+56985639791', 'Av. República #8277', 'Ñuñoa', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '17.853.615-K', 'natural', NULL, NULL),
(145, 'Jorge Reyes', 'jorge.reyes@email.com', '+56992306196', 'Pasaje Libertador #9425', 'Punta Arenas', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '24.837.623-6', 'natural', NULL, NULL),
(146, 'Andrés González', 'andrés.gonzález@email.com', '+56989627025', 'Pasaje Libertador #5962', 'Iquique', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '8.695.067-7', 'natural', NULL, NULL),
(147, 'Claudia Torres', 'claudia.torres@email.com', '+56916647447', 'Calle Libertador #403', 'La Florida', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '24.799.263-4', 'natural', NULL, NULL),
(148, 'Isabel Flores', 'isabel.flores@email.com', '+56977056532', 'Pasaje Independencia #6619', 'Coquimbo', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '10.272.845-9', 'natural', NULL, NULL),
(149, 'Valentina Jiménez', 'valentina.jiménez@email.com', '+56918041204', 'Av. Constitución #8059', 'Ñuñoa', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '24.348.333-6', 'natural', NULL, NULL),
(150, 'Carlos Torres', 'carlos.torres@email.com', '+56971494729', 'Calle Independencia #2503', 'Iquique', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '5.870.350-8', 'natural', NULL, NULL),
(151, 'Lorena Araya', 'lorena.araya@email.com', '+56937165224', 'Av. Libertador #8109', 'Las Condes', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '17.233.650-7', 'natural', NULL, NULL),
(152, 'Elena Contreras', 'elena.contreras@email.com', '+56954348580', 'Calle Libertador #2897', 'Providencia', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '7.973.822-0', 'natural', NULL, NULL),
(153, 'Katherine Ramírez', 'katherine.ramírez@email.com', '+56959591434', 'Pasaje República #5733', 'Providencia', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '4.010.918-8', 'natural', NULL, NULL),
(154, 'José Vásquez', 'josé.vásquez@email.com', '+56937200972', 'Pasaje Libertador #7417', 'Ñuñoa', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '18.233.002-7', 'natural', NULL, NULL),
(155, 'Cristian López', 'cristian.lópez@email.com', '+56919574058', 'Pasaje República #924', 'Temuco', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '20.174.123-8', 'natural', NULL, NULL),
(156, 'Gonzalo Fuentes', 'gonzalo.fuentes@email.com', '+56952081581', 'Pasaje República #4745', 'Puerto Montt', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '17.706.082-8', 'natural', NULL, NULL),
(157, 'Marcela Parra', 'marcela.parra@email.com', '+56917317100', 'Calle Independencia #498', 'La Florida', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '19.526.642-5', 'natural', NULL, NULL),
(158, 'Elena Núñez', 'elena.núñez@email.com', '+56951765562', 'Av. Independencia #3246', 'Viña del Mar', 'Valparaíso', '2025-10-07', 'Consumidor Final', NULL, '20.642.539-3', 'natural', NULL, NULL),
(159, 'Patricia Cortés', 'patricia.cortés@email.com', '+56994181764', 'Calle Constitución #6157', 'Santiago', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '17.037.082-1', 'natural', NULL, NULL),
(160, 'Isabel Herrera', 'isabel.herrera@email.com', '+56994083375', 'Av. Libertador #3168', 'Talca', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '12.089.250-9', 'natural', NULL, NULL),
(161, 'Fernando Sánchez', 'fernando.sánchez@email.com', '+56925002946', 'Av. República #6786', 'Rancagua', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '18.094.601-2', 'natural', NULL, NULL),
(162, 'Javiera Carrasco', 'javiera.carrasco@email.com', '+56991572489', 'Pasaje Independencia #4656', 'Providencia', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '17.516.920-2', 'natural', NULL, NULL),
(163, 'Francisco Sepúlveda', 'francisco.sepúlveda@email.com', '+56926272728', 'Calle Libertador #3663', 'Antofagasta', 'Ñuble', '2025-10-07', 'Consumidor Final', NULL, '19.185.498-5', 'natural', NULL, NULL),
(164, 'Laura Jiménez', 'laura.jiménez@email.com', '+56969214389', 'Av. Constitución #8520', 'Puerto Montt', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '8.649.615-1', 'natural', NULL, NULL),
(165, 'Sofía López', 'sofía.lópez@email.com', '+56985674859', 'Av. Constitución #1640', 'La Serena', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '9.529.569-K', 'natural', NULL, NULL),
(166, 'Fernando Rojas', 'fernando.rojas@email.com', '+56966479905', 'Pasaje Libertador #8670', 'Antofagasta', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '4.845.100-4', 'natural', NULL, NULL),
(167, 'Eduardo González', 'eduardo.gonzález@email.com', '+56972966688', 'Calle Independencia #4772', 'Osorno', 'Biobío', '2025-10-07', 'Empresa', NULL, '2.951.953-6', 'natural', NULL, NULL),
(168, 'Sofía Morales', 'sofía.morales@email.com', '+56937645704', 'Pasaje Independencia #6841', 'Puente Alto', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '16.974.195-6', 'natural', NULL, NULL),
(169, 'Elena Parra', 'elena.parra@email.com', '+56946110372', 'Av. Independencia #1573', 'La Serena', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '15.590.262-0', 'natural', NULL, NULL),
(170, 'Javiera Gutiérrez', 'javiera.gutiérrez@email.com', '+56984682277', 'Av. Constitución #1015', 'Puerto Montt', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '22.263.622-1', 'natural', NULL, NULL),
(171, 'Gonzalo Tapia', 'gonzalo.tapia@email.com', '+56928363766', 'Pasaje Libertador #8354', 'Iquique', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '19.688.593-5', 'natural', NULL, NULL),
(172, 'Javier Ramírez', 'javier.ramírez@email.com', '+56944860969', 'Calle República #2443', 'Coquimbo', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '5.819.679-7', 'natural', NULL, NULL),
(173, 'María Muñoz', 'maría.muñoz@email.com', '+56926929925', 'Calle República #412', 'Valparaíso', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '13.514.678-1', 'natural', NULL, NULL),
(174, 'Elena Araya', 'elena.araya@email.com', '+56999419762', 'Av. República #6287', 'Concepción', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '5.523.560-0', 'natural', NULL, NULL),
(175, 'Sofía Flores', 'sofía.flores@email.com', '+56967733311', 'Calle Libertador #8965', 'Coquimbo', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '19.281.510-K', 'natural', NULL, NULL),
(176, 'Héctor Contreras', 'héctor.contreras@email.com', '+56991476772', 'Pasaje Constitución #4183', 'Osorno', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '12.611.523-7', 'natural', NULL, NULL),
(177, 'Carmen Sepúlveda', 'carmen.sepúlveda@email.com', '+56958857961', 'Calle Independencia #4893', 'Las Condes', 'Maule', '2025-10-07', 'Contribuyente', NULL, '24.866.074-0', 'natural', NULL, NULL),
(178, 'Antonio Cortés', 'antonio.cortés@email.com', '+56935590099', 'Pasaje Constitución #9928', 'Puente Alto', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '4.343.240-0', 'natural', NULL, NULL),
(179, 'Javiera Hernández', 'javiera.hernández@email.com', '+56933142128', 'Av. Libertador #9297', 'Antofagasta', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '6.988.251-K', 'natural', NULL, NULL),
(180, 'Isabel Reyes', 'isabel.reyes@email.com', '+56925523158', 'Pasaje Constitución #8373', 'Talca', 'Biobío', '2025-10-07', 'Empresa', NULL, '21.885.344-7', 'natural', NULL, NULL),
(181, 'Isabel Núñez', 'isabel.núñez@email.com', '+56931798107', 'Pasaje Libertador #1638', 'Las Condes', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '3.781.580-2', 'natural', NULL, NULL),
(182, 'Lorena Rodríguez', 'lorena.rodríguez@email.com', '+56987816513', 'Av. Constitución #728', 'Iquique', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '9.419.427-K', 'natural', NULL, NULL),
(183, 'Juan Pérez', 'juan.pérez@email.com', '+56956251866', 'Calle Libertador #1029', 'Coquimbo', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '14.243.698-1', 'natural', NULL, NULL),
(184, 'Carlos Rojas', 'carlos.rojas@email.com', '+56948848843', 'Calle República #3470', 'Talca', 'Biobío', '2025-10-07', 'Empresa', NULL, '11.516.746-4', 'natural', NULL, NULL),
(185, 'Javiera Álvarez', 'javiera.álvarez@email.com', '+56935729844', 'Pasaje Constitución #6842', 'Ñuñoa', 'Coquimbo', '2025-10-07', 'Contribuyente', NULL, '24.481.165-5', 'natural', NULL, NULL),
(186, 'Claudia Torres', 'claudia.torres@email.com', '+56963830630', 'Pasaje República #9540', 'Osorno', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '1.656.869-4', 'natural', NULL, NULL),
(187, 'Verónica Fuentes', 'verónica.fuentes@email.com', '+56994678500', 'Calle Constitución #5204', 'Rancagua', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '14.985.597-1', 'natural', NULL, NULL),
(188, 'Héctor Rojas', 'héctor.rojas@email.com', '+56960161112', 'Av. Independencia #2950', 'Providencia', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '16.191.721-4', 'natural', NULL, NULL),
(189, 'Ignacio Sepúlveda', 'ignacio.sepúlveda@email.com', '+56963166711', 'Pasaje Constitución #3487', 'Coquimbo', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '14.924.117-5', 'natural', NULL, NULL),
(190, 'Andrés Soto', 'andrés.soto@email.com', '+56966369213', 'Calle República #5959', 'Concepción', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '7.748.341-1', 'natural', NULL, NULL),
(191, 'Ignacio Sánchez', 'ignacio.sánchez@email.com', '+56931615631', 'Calle República #6707', 'Concepción', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '11.035.702-8', 'natural', NULL, NULL),
(192, 'Paula Flores', 'paula.flores@email.com', '+56944454280', 'Av. Constitución #4886', 'Punta Arenas', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '14.661.339-K', 'natural', NULL, NULL),
(193, 'Javier González', 'javier.gonzález@email.com', '+56933189503', 'Calle República #8501', 'San Bernardo', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '16.319.771-5', 'natural', NULL, NULL),
(194, 'Antonio Núñez', 'antonio.núñez@email.com', '+56926483461', 'Av. Independencia #8750', 'Valparaíso', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '6.346.712-K', 'natural', NULL, NULL),
(195, 'Valentina Castillo', 'valentina.castillo@email.com', '+56926594444', 'Calle República #9431', 'La Serena', 'Magallanes', '2025-10-07', 'Empresa', NULL, '8.383.413-7', 'natural', NULL, NULL),
(196, 'Fernando Torres', 'fernando.torres@email.com', '+56912236056', 'Av. Constitución #1009', 'Concepción', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '21.987.481-2', 'natural', NULL, NULL),
(197, 'Javiera Rojas', 'javiera.rojas@email.com', '+56963839415', 'Av. Constitución #4255', 'San Bernardo', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '9.403.676-3', 'natural', NULL, NULL),
(198, 'Javiera Fernández', 'javiera.fernández@email.com', '+56963027039', 'Calle Constitución #3477', 'Antofagasta', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '15.132.246-8', 'natural', NULL, NULL),
(199, 'Eduardo Ramírez', 'eduardo.ramírez@email.com', '+56986099422', 'Pasaje Libertador #6575', 'La Florida', 'Metropolitana', '2025-10-07', 'Consumidor Final', NULL, '7.499.926-3', 'natural', NULL, NULL),
(200, 'Eduardo Vásquez', 'eduardo.vásquez@email.com', '+56997181437', 'Av. República #6838', 'Temuco', 'Biobío', '2025-10-07', 'Empresa', NULL, '8.416.331-7', 'natural', NULL, NULL),
(201, 'Claudia López', 'claudia.lópez@email.com', '+56917001512', 'Pasaje Constitución #4233', 'Santiago', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '3.208.987-9', 'natural', NULL, NULL),
(202, 'Antonio Díaz', 'antonio.díaz@email.com', '+56947210150', 'Calle República #5200', 'Rancagua', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '7.292.052-K', 'natural', NULL, NULL),
(203, 'Lorena Vargas', 'lorena.vargas@email.com', '+56920679907', 'Av. Libertador #8385', 'Iquique', 'Biobío', '2025-10-07', 'Empresa', NULL, '3.632.497-K', 'natural', NULL, NULL),
(204, 'Eduardo Hernández', 'eduardo.hernández@email.com', '+56958420185', 'Av. Constitución #3729', 'Punta Arenas', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '2.863.248-7', 'natural', NULL, NULL),
(205, 'Isabel Vásquez', 'isabel.vásquez@email.com', '+56925627346', 'Av. Independencia #462', 'Puente Alto', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '8.347.026-7', 'natural', NULL, NULL),
(206, 'Lorena Silva', 'lorena.silva@email.com', '+56939342765', 'Pasaje Constitución #4382', 'Providencia', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '23.572.093-0', 'natural', NULL, NULL),
(207, 'Francisco Parra', 'francisco.parra@email.com', '+56959120013', 'Calle Independencia #8747', 'Rancagua', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '10.109.865-6', 'natural', NULL, NULL),
(208, 'Isabel Contreras', 'isabel.contreras@email.com', '+56999314527', 'Calle República #6544', 'Coquimbo', 'Valparaíso', '2025-10-07', 'Consumidor Final', NULL, '17.182.699-3', 'natural', NULL, NULL),
(209, 'Francisca Ramírez', 'francisca.ramírez@email.com', '+56966175477', 'Av. República #5419', 'Chillán', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '18.367.603-2', 'natural', NULL, NULL),
(210, 'Andrés Jiménez', 'andrés.jiménez@email.com', '+56955491263', 'Av. Constitución #3500', 'Concepción', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '2.082.987-7', 'natural', NULL, NULL),
(211, 'Rosa Sepúlveda', 'rosa.sepúlveda@email.com', '+56918684949', 'Pasaje Libertador #7798', 'Providencia', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '12.240.440-4', 'natural', NULL, NULL),
(212, 'Sandra Gómez', 'sandra.gómez@email.com', '+56954273017', 'Pasaje República #9309', 'Viña del Mar', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '22.917.695-1', 'natural', NULL, NULL),
(213, 'Jorge Silva', 'jorge.silva@email.com', '+56974493943', 'Calle República #6522', 'Providencia', 'Maule', '2025-10-07', 'Contribuyente', NULL, '1.288.326-9', 'natural', NULL, NULL),
(214, 'Antonio Ramírez', 'antonio.ramírez@email.com', '+56974359235', 'Pasaje Libertador #4436', 'Iquique', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '1.517.267-3', 'natural', NULL, NULL),
(215, 'Claudia Muñoz', 'claudia.muñoz@email.com', '+56970524114', 'Av. República #7906', 'La Florida', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '17.672.925-2', 'natural', NULL, NULL),
(216, 'Javiera Silva', 'javiera.silva@email.com', '+56980091955', 'Pasaje Constitución #1707', 'Iquique', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '16.582.421-0', 'natural', NULL, NULL),
(217, 'Patricia Parra', 'patricia.parra@email.com', '+56923599852', 'Pasaje Independencia #4448', 'Viña del Mar', 'Biobío', '2025-10-07', 'Empresa', NULL, '8.330.552-5', 'natural', NULL, NULL),
(218, 'Paula Díaz', 'paula.díaz@email.com', '+56914344758', 'Pasaje República #6006', 'Concepción', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '14.200.378-3', 'natural', NULL, NULL),
(219, 'Isabel Sánchez', 'isabel.sánchez@email.com', '+56943122522', 'Av. Libertador #9745', 'Valparaíso', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '20.698.528-3', 'natural', NULL, NULL),
(220, 'Valentina Carrasco', 'valentina.carrasco@email.com', '+56992663807', 'Pasaje Libertador #1380', 'Osorno', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '18.835.443-2', 'natural', NULL, NULL),
(221, 'Claudia Araya', 'claudia.araya@email.com', '+56968936831', 'Av. Independencia #4142', 'Coquimbo', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '17.345.403-1', 'natural', NULL, NULL),
(222, 'Fernando Contreras', 'fernando.contreras@email.com', '+56916446661', 'Pasaje Independencia #3254', 'Las Condes', 'Metropolitana', '2025-10-07', 'Consumidor Final', NULL, '21.539.796-3', 'natural', NULL, NULL),
(223, 'Ignacio Carrasco', 'ignacio.carrasco@email.com', '+56975619670', 'Pasaje República #2373', 'Valparaíso', 'Metropolitana', '2025-10-07', 'Consumidor Final', NULL, '10.838.816-1', 'natural', NULL, NULL),
(224, 'Alejandro Parra', 'alejandro.parra@email.com', '+56941879729', 'Av. Libertador #9456', 'Concepción', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '20.464.331-8', 'natural', NULL, NULL),
(225, 'Francisca Castillo', 'francisca.castillo@email.com', '+56955501080', 'Av. Constitución #4263', 'Punta Arenas', 'Coquimbo', '2025-10-07', 'Contribuyente', NULL, '4.572.885-4', 'natural', NULL, NULL),
(226, 'Sandra Núñez', 'sandra.núñez@email.com', '+56980611559', 'Pasaje Independencia #1938', 'Iquique', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '10.671.814-8', 'natural', NULL, NULL),
(227, 'Andrés Rodríguez', 'andrés.rodríguez@email.com', '+56983605577', 'Calle República #7348', 'Providencia', 'Maule', '2025-10-07', 'Contribuyente', NULL, '20.748.100-9', 'natural', NULL, NULL),
(228, 'Javiera Castillo', 'javiera.castillo@email.com', '+56930035663', 'Calle Constitución #7914', 'Viña del Mar', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '18.043.749-5', 'natural', NULL, NULL),
(229, 'Eduardo Gómez', 'eduardo.gómez@email.com', '+56966713449', 'Av. Constitución #4199', 'La Florida', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '3.282.117-0', 'natural', NULL, NULL),
(230, 'Daniel Morales', 'daniel.morales@email.com', '+56915654658', 'Av. República #5773', 'Rancagua', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '12.126.077-8', 'natural', NULL, NULL),
(231, 'Fernando Ramírez', 'fernando.ramírez@email.com', '+56944617058', 'Pasaje Independencia #9569', 'Punta Arenas', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '9.187.329-K', 'natural', NULL, NULL),
(232, 'Diego Morales', 'diego.morales@email.com', '+56956166517', 'Av. Libertador #1917', 'Concepción', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '18.096.162-3', 'natural', NULL, NULL),
(233, 'Marcela Álvarez', 'marcela.álvarez@email.com', '+56912836063', 'Pasaje Libertador #7845', 'Coquimbo', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '10.220.047-0', 'natural', NULL, NULL),
(234, 'Cristian Martínez', 'cristian.martínez@email.com', '+56912818447', 'Pasaje República #6730', 'Rancagua', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '22.048.412-2', 'natural', NULL, NULL),
(235, 'José Moreno', 'josé.moreno@email.com', '+56987457291', 'Calle Constitución #9195', 'Coquimbo', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '18.122.612-9', 'natural', NULL, NULL),
(236, 'Cristian Hernández', 'cristian.hernández@email.com', '+56989688995', 'Calle República #1960', 'Las Condes', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '7.752.989-6', 'natural', NULL, NULL),
(237, 'Jorge Vargas', 'jorge.vargas@email.com', '+56921080234', 'Av. Constitución #6751', 'La Florida', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '19.539.923-9', 'natural', NULL, NULL),
(238, 'José Valenzuela', 'josé.valenzuela@email.com', '+56945717948', 'Pasaje Libertador #4639', 'Talca', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '18.514.111-K', 'natural', NULL, NULL),
(239, 'Alejandro Morales', 'alejandro.morales@email.com', '+56964739522', 'Calle Libertador #5421', 'Concepción', 'Ñuble', '2025-10-07', 'Empresa', NULL, '12.495.677-3', 'natural', NULL, NULL),
(240, 'Carlos Torres', 'carlos.torres@email.com', '+56920131508', 'Av. Libertador #927', 'Talca', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '3.389.766-9', 'natural', NULL, NULL),
(241, 'María Tapia', 'maría.tapia@email.com', '+56947385177', 'Calle Libertador #6819', 'La Serena', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '5.727.344-5', 'natural', NULL, NULL),
(242, 'Marcela Espinoza', 'marcela.espinoza@email.com', '+56982376127', 'Pasaje Libertador #1501', 'Santiago', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '3.070.362-6', 'natural', NULL, NULL),
(243, 'Luis Fuentes', 'luis.fuentes@email.com', '+56971098926', 'Av. República #6750', 'La Serena', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '18.848.459-K', 'natural', NULL, NULL),
(244, 'Paula Carrasco', 'paula.carrasco@email.com', '+56984319007', 'Av. Libertador #4077', 'Osorno', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '5.507.030-K', 'natural', NULL, NULL),
(245, 'Gabriel Hernández', 'gabriel.hernández@email.com', '+56981062668', 'Pasaje República #7342', 'Concepción', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '3.378.139-3', 'natural', NULL, NULL),
(246, 'Valentina Araya', 'valentina.araya@email.com', '+56981925303', 'Pasaje Libertador #3095', 'Las Condes', 'Coquimbo', '2025-10-07', 'Contribuyente', NULL, '11.394.257-6', 'natural', NULL, NULL),
(247, 'Ignacio Moreno', 'ignacio.moreno@email.com', '+56999772629', 'Calle Constitución #6903', 'Valparaíso', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '7.895.496-5', 'natural', NULL, NULL),
(248, 'Francisco Carrasco', 'francisco.carrasco@email.com', '+56929771855', 'Pasaje Independencia #6759', 'Punta Arenas', 'Araucanía', '2025-10-07', 'Consumidor Final', NULL, '8.026.993-5', 'natural', NULL, NULL),
(249, 'Fernando Cortés', 'fernando.cortés@email.com', '+56964180450', 'Calle Libertador #5070', 'San Bernardo', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '1.304.410-4', 'natural', NULL, NULL),
(250, 'Carmen Hernández', 'carmen.hernández@email.com', '+56986472635', 'Calle Libertador #6827', 'Concepción', 'Ñuble', '2025-10-07', 'Empresa', NULL, '1.208.158-8', 'natural', NULL, NULL),
(251, 'Sandra Herrera', 'sandra.herrera@email.com', '+56930037524', 'Calle República #4207', 'Puente Alto', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '7.847.239-1', 'natural', NULL, NULL),
(252, 'Isabel Sepúlveda', 'isabel.sepúlveda@email.com', '+56921666744', 'Pasaje Libertador #6702', 'La Serena', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '1.411.295-2', 'natural', NULL, NULL),
(253, 'Sandra Fernández', 'sandra.fernández@email.com', '+56937010972', 'Pasaje Independencia #9179', 'Temuco', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '23.581.983-K', 'natural', NULL, NULL),
(254, 'Cristian Rojas', 'cristian.rojas@email.com', '+56976506875', 'Pasaje Independencia #8619', 'Rancagua', 'Magallanes', '2025-10-07', 'Empresa', NULL, '9.898.321-K', 'natural', NULL, NULL),
(255, 'Javiera Martínez', 'javiera.martínez@email.com', '+56977429291', 'Av. Libertador #1451', 'Ñuñoa', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '3.606.015-8', 'natural', NULL, NULL),
(256, 'Elena Muñoz', 'elena.muñoz@email.com', '+56975412032', 'Calle Independencia #589', 'Osorno', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '3.396.982-1', 'natural', NULL, NULL);
INSERT INTO `djangoVerVictorMondaca_clientes` (`id`, `nombre`, `email`, `telefono`, `direccion`, `comuna`, `region`, `fecha_registro`, `tipo_cliente`, `observaciones`, `rut`, `tipo_persona`, `giro`, `contacto`) VALUES
(257, 'Antonio Vásquez', 'antonio.vásquez@email.com', '+56997184277', 'Calle Independencia #1666', 'Ñuñoa', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '10.955.123-6', 'natural', NULL, NULL),
(258, 'Claudia Soto', 'claudia.soto@email.com', '+56931523403', 'Calle Constitución #6002', 'Puente Alto', 'Ñuble', '2025-10-07', 'Consumidor Final', NULL, '9.948.119-6', 'natural', NULL, NULL),
(259, 'Juan Rodríguez', 'juan.rodríguez@email.com', '+56974223186', 'Calle Constitución #2671', 'La Serena', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '14.515.868-0', 'natural', NULL, NULL),
(260, 'Carlos González', 'carlos.gonzález@email.com', '+56990233424', 'Av. Constitución #9865', 'Puente Alto', 'Biobío', '2025-10-07', 'Empresa', NULL, '2.790.795-4', 'natural', NULL, NULL),
(261, 'Manuel Fuentes', 'manuel.fuentes@email.com', '+56964932592', 'Calle Independencia #512', 'Antofagasta', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '4.715.755-2', 'natural', NULL, NULL),
(262, 'Carlos Ramírez', 'carlos.ramírez@email.com', '+56962423124', 'Pasaje Independencia #8204', 'Osorno', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '16.222.911-7', 'natural', NULL, NULL),
(263, 'Gonzalo Rodríguez', 'gonzalo.rodríguez@email.com', '+56911144679', 'Pasaje Constitución #9721', 'Osorno', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '14.959.419-1', 'natural', NULL, NULL),
(264, 'Verónica Álvarez', 'verónica.álvarez@email.com', '+56971388139', 'Av. Independencia #2806', 'Rancagua', 'Maule', '2025-10-07', 'Contribuyente', NULL, '24.332.868-3', 'natural', NULL, NULL),
(265, 'Claudia Martínez', 'claudia.martínez@email.com', '+56923733810', 'Calle Libertador #5396', 'Temuco', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '23.641.650-K', 'natural', NULL, NULL),
(266, 'José Contreras', 'josé.contreras@email.com', '+56917006669', 'Pasaje Libertador #8503', 'Valparaíso', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '22.204.736-6', 'natural', NULL, NULL),
(267, 'Javiera Sánchez', 'javiera.sánchez@email.com', '+56935474525', 'Calle Libertador #6624', 'San Bernardo', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '19.415.234-5', 'natural', NULL, NULL),
(268, 'Luis Araya', 'luis.araya@email.com', '+56912099888', 'Pasaje Independencia #9652', 'Viña del Mar', 'Maule', '2025-10-07', 'Empresa', NULL, '10.324.290-8', 'natural', NULL, NULL),
(269, 'Elena Morales', 'elena.morales@email.com', '+56957142948', 'Pasaje República #2940', 'La Serena', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '17.783.671-0', 'natural', NULL, NULL),
(270, 'Daniel Núñez', 'daniel.núñez@email.com', '+56911184669', 'Av. Constitución #5837', 'Santiago', 'Araucanía', '2025-10-07', 'Empresa', NULL, '11.840.918-3', 'natural', NULL, NULL),
(271, 'Sandra Morales', 'sandra.morales@email.com', '+56926473284', 'Pasaje Constitución #5343', 'San Bernardo', 'Metropolitana', '2025-10-07', 'Consumidor Final', NULL, '10.803.937-K', 'natural', NULL, NULL),
(272, 'José Contreras', 'josé.contreras@email.com', '+56997423603', 'Av. Constitución #2083', 'Las Condes', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '6.158.640-7', 'natural', NULL, NULL),
(273, 'Laura Silva', 'laura.silva@email.com', '+56955779857', 'Av. Libertador #7972', 'Punta Arenas', 'Los Lagos', '2025-10-07', 'Contribuyente', NULL, '21.022.454-8', 'natural', NULL, NULL),
(274, 'Héctor Morales', 'héctor.morales@email.com', '+56965936532', 'Calle República #7556', 'Antofagasta', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '21.683.900-5', 'natural', NULL, NULL),
(275, 'Isabel Cortés', 'isabel.cortés@email.com', '+56959212011', 'Calle República #3149', 'Providencia', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '11.155.378-5', 'natural', NULL, NULL),
(276, 'Katherine Rodríguez', 'katherine.rodríguez@email.com', '+56982196658', 'Av. República #3257', 'Santiago', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '15.036.356-K', 'natural', NULL, NULL),
(277, 'Lorena Herrera', 'lorena.herrera@email.com', '+56996097237', 'Av. Libertador #8324', 'Concepción', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '19.078.627-7', 'natural', NULL, NULL),
(278, 'Antonio Sánchez', 'antonio.sánchez@email.com', '+56993087088', 'Av. Independencia #2309', 'Providencia', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '9.956.611-6', 'natural', NULL, NULL),
(279, 'María Araya', 'maría.araya@email.com', '+56993797798', 'Av. Constitución #1712', 'San Bernardo', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '19.912.447-1', 'natural', NULL, NULL),
(280, 'Carlos Vásquez', 'carlos.vásquez@email.com', '+56961107626', 'Pasaje Constitución #3614', 'Temuco', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '8.691.983-4', 'natural', NULL, NULL),
(281, 'Sofía Pérez', 'sofía.pérez@email.com', '+56974250320', 'Pasaje Constitución #2476', 'Arica', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '10.046.221-4', 'natural', NULL, NULL),
(282, 'Diego Díaz', 'diego.díaz@email.com', '+56982439380', 'Calle Independencia #2835', 'Puerto Montt', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '14.189.243-6', 'natural', NULL, NULL),
(283, 'Francisca Jiménez', 'francisca.jiménez@email.com', '+56920821459', 'Calle República #408', 'Puerto Montt', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '17.794.350-9', 'natural', NULL, NULL),
(284, 'Francisca Gutiérrez', 'francisca.gutiérrez@email.com', '+56934208104', 'Pasaje Constitución #4037', 'Concepción', 'Maule', '2025-10-07', 'Contribuyente', NULL, '13.839.893-5', 'natural', NULL, NULL),
(285, 'José Gutiérrez', 'josé.gutiérrez@email.com', '+56971328887', 'Av. Constitución #4362', 'Antofagasta', 'Magallanes', '2025-10-07', 'Empresa', NULL, '24.023.889-6', 'natural', NULL, NULL),
(286, 'Paula Carrasco', 'paula.carrasco@email.com', '+56940386558', 'Pasaje Independencia #2210', 'Chillán', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '6.263.272-0', 'natural', NULL, NULL),
(287, 'Elena Cortés', 'elena.cortés@email.com', '+56992480088', 'Av. Independencia #5918', 'Santiago', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '13.306.069-3', 'natural', NULL, NULL),
(288, 'Claudia Moreno', 'claudia.moreno@email.com', '+56933874705', 'Av. República #5892', 'La Florida', 'Araucanía', '2025-10-07', 'Empresa', NULL, '6.293.852-8', 'natural', NULL, NULL),
(289, 'Patricia Espinoza', 'patricia.espinoza@email.com', '+56950466854', 'Pasaje Independencia #4582', 'Ñuñoa', 'Maule', '2025-10-07', 'Contribuyente', NULL, '4.839.161-3', 'natural', NULL, NULL),
(290, 'Laura Morales', 'laura.morales@email.com', '+56986105910', 'Pasaje Constitución #5529', 'Las Condes', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '9.356.372-7', 'natural', NULL, NULL),
(291, 'Carlos Soto', 'carlos.soto@email.com', '+56957835388', 'Av. República #9066', 'Puerto Montt', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '20.626.017-3', 'natural', NULL, NULL),
(292, 'Daniel Muñoz', 'daniel.muñoz@email.com', '+56940695548', 'Av. Independencia #2263', 'Valparaíso', 'Ñuble', '2025-10-07', 'Empresa', NULL, '8.840.619-2', 'natural', NULL, NULL),
(293, 'Katherine Fuentes', 'katherine.fuentes@email.com', '+56996734123', 'Calle Libertador #7651', 'Osorno', 'Valparaíso', '2025-10-07', 'Consumidor Final', NULL, '9.381.987-K', 'natural', NULL, NULL),
(294, 'Valentina Espinoza', 'valentina.espinoza@email.com', '+56995571096', 'Calle Libertador #3063', 'Punta Arenas', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '3.957.830-1', 'natural', NULL, NULL),
(295, 'Rosa Carrasco', 'rosa.carrasco@email.com', '+56923446685', 'Pasaje Independencia #3328', 'San Bernardo', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '13.362.353-1', 'natural', NULL, NULL),
(296, 'Alejandro Díaz', 'alejandro.díaz@email.com', '+56919074009', 'Av. Constitución #6596', 'Arica', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '2.411.763-4', 'natural', NULL, NULL),
(297, 'Andrés Muñoz', 'andrés.muñoz@email.com', '+56923380110', 'Calle Independencia #4853', 'La Serena', 'Valparaíso', '2025-10-07', 'Consumidor Final', NULL, '9.122.421-6', 'natural', NULL, NULL),
(298, 'Jorge Vargas', 'jorge.vargas@email.com', '+56985187673', 'Calle Constitución #960', 'Osorno', 'Ñuble', '2025-10-07', 'Empresa', NULL, '19.656.626-0', 'natural', NULL, NULL),
(299, 'Daniel Rodríguez', 'daniel.rodríguez@email.com', '+56926532070', 'Pasaje Constitución #2842', 'Talca', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '4.605.746-5', 'natural', NULL, NULL),
(300, 'Alejandro Valenzuela', 'alejandro.valenzuela@email.com', '+56934944080', 'Av. República #8796', 'Talca', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '17.881.817-1', 'natural', NULL, NULL),
(301, 'Cristian Herrera', 'cristian.herrera@email.com', '+56984657381', 'Calle Constitución #4794', 'Chillán', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '19.634.621-K', 'natural', NULL, NULL),
(302, 'Daniel Moreno', 'daniel.moreno@email.com', '+56947903547', 'Av. República #5533', 'La Florida', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '21.223.215-7', 'natural', NULL, NULL),
(303, 'Gabriel Vargas', 'gabriel.vargas@email.com', '+56990477486', 'Pasaje Independencia #9313', 'Concepción', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '17.471.103-8', 'natural', NULL, NULL),
(304, 'Paula Flores', 'paula.flores@email.com', '+56925189986', 'Av. República #2940', 'Iquique', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '13.074.849-K', 'natural', NULL, NULL),
(305, 'Sofía Castillo', 'sofía.castillo@email.com', '+56911657680', 'Pasaje Libertador #561', 'Temuco', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '5.880.468-1', 'natural', NULL, NULL),
(306, 'Patricia Martínez', 'patricia.martínez@email.com', '+56950678584', 'Calle Independencia #3482', 'Puerto Montt', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '19.904.325-0', 'natural', NULL, NULL),
(307, 'Paula Fernández', 'paula.fernández@email.com', '+56999669910', 'Av. Independencia #5844', 'Arica', 'Coquimbo', '2025-10-07', 'Empresa', NULL, '10.606.910-7', 'natural', NULL, NULL),
(308, 'Patricia Sánchez', 'patricia.sánchez@email.com', '+56981160522', 'Pasaje Libertador #3169', 'Santiago', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '12.510.637-4', 'natural', NULL, NULL),
(309, 'Ana Gutiérrez', 'ana.gutiérrez@email.com', '+56996753294', 'Av. Libertador #2394', 'La Serena', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '12.097.062-3', 'natural', NULL, NULL),
(310, 'Gonzalo Pérez', 'gonzalo.pérez@email.com', '+56994318476', 'Pasaje Libertador #1591', 'La Florida', 'Araucanía', '2025-10-07', 'Consumidor Final', NULL, '17.045.224-0', 'natural', NULL, NULL),
(311, 'Javier Tapia', 'javier.tapia@email.com', '+56924625129', 'Pasaje Independencia #9465', 'Temuco', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '8.371.000-4', 'natural', NULL, NULL),
(312, 'Natalia Tapia', 'natalia.tapia@email.com', '+56912093898', 'Pasaje Libertador #6786', 'Puerto Montt', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '20.365.045-0', 'natural', NULL, NULL),
(313, 'Andrés Moreno', 'andrés.moreno@email.com', '+56982167810', 'Av. Constitución #6944', 'Maipú', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '19.223.068-3', 'natural', NULL, NULL),
(314, 'Cristian Díaz', 'cristian.díaz@email.com', '+56914757562', 'Av. Constitución #6825', 'Puerto Montt', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '4.622.309-8', 'natural', NULL, NULL),
(315, 'Gonzalo Pérez', 'gonzalo.pérez@email.com', '+56947564178', 'Calle Libertador #4649', 'Ñuñoa', 'Coquimbo', '2025-10-07', 'Contribuyente', NULL, '3.065.890-6', 'natural', NULL, NULL),
(316, 'Gabriel Castro', 'gabriel.castro@email.com', '+56970718080', 'Calle República #6612', 'Concepción', 'Maule', '2025-10-07', 'Contribuyente', NULL, '15.933.668-9', 'natural', NULL, NULL),
(317, 'Daniel Espinoza', 'daniel.espinoza@email.com', '+56915912908', 'Calle Libertador #6899', 'Chillán', 'Magallanes', '2025-10-07', 'Empresa', NULL, '17.632.535-6', 'natural', NULL, NULL),
(318, 'Andrés Reyes', 'andrés.reyes@email.com', '+56993310521', 'Calle República #6532', 'Concepción', 'Biobío', '2025-10-07', 'Empresa', NULL, '9.032.741-0', 'natural', NULL, NULL),
(319, 'Alejandro Ramírez', 'alejandro.ramírez@email.com', '+56998181243', 'Calle Constitución #9240', 'Rancagua', 'Coquimbo', '2025-10-07', 'Empresa', NULL, '2.604.853-2', 'natural', NULL, NULL),
(320, 'Fernando Herrera', 'fernando.herrera@email.com', '+56952308310', 'Pasaje Libertador #2041', 'Puente Alto', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '6.365.737-9', 'natural', NULL, NULL),
(321, 'Diego Valenzuela', 'diego.valenzuela@email.com', '+56921934143', 'Pasaje Independencia #8840', 'Maipú', 'Ñuble', '2025-10-07', 'Consumidor Final', NULL, '13.754.127-0', 'natural', NULL, NULL),
(322, 'Diego Espinoza', 'diego.espinoza@email.com', '+56946939587', 'Calle República #2345', 'Santiago', 'Coquimbo', '2025-10-07', 'Empresa', NULL, '24.335.094-8', 'natural', NULL, NULL),
(323, 'Luis López', 'luis.lópez@email.com', '+56976082343', 'Av. Constitución #1878', 'Arica', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '21.010.798-3', 'natural', NULL, NULL),
(324, 'Sofía Moreno', 'sofía.moreno@email.com', '+56948300750', 'Av. Constitución #3968', 'Puente Alto', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '20.950.649-1', 'natural', NULL, NULL),
(325, 'Eduardo Valenzuela', 'eduardo.valenzuela@email.com', '+56990980106', 'Calle República #7328', 'Providencia', 'Coquimbo', '2025-10-07', 'Contribuyente', NULL, '24.735.719-K', 'natural', NULL, NULL),
(326, 'Paula Espinoza', 'paula.espinoza@email.com', '+56921171990', 'Av. República #9186', 'Puente Alto', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '19.061.445-K', 'natural', NULL, NULL),
(327, 'Cristian González', 'cristian.gonzález@email.com', '+56987583343', 'Av. Libertador #7717', 'San Bernardo', 'Metropolitana', '2025-10-07', 'Consumidor Final', NULL, '6.842.252-3', 'natural', NULL, NULL),
(328, 'Gonzalo Díaz', 'gonzalo.díaz@email.com', '+56960229275', 'Pasaje Independencia #8008', 'Las Condes', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '21.123.065-7', 'natural', NULL, NULL),
(329, 'Antonio Parra', 'antonio.parra@email.com', '+56972527287', 'Pasaje Constitución #7663', 'Rancagua', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '12.229.211-8', 'natural', NULL, NULL),
(330, 'Manuel Hernández', 'manuel.hernández@email.com', '+56981036665', 'Av. Constitución #3736', 'La Serena', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '5.731.091-K', 'natural', NULL, NULL),
(331, 'Ana Muñoz', 'ana.muñoz@email.com', '+56993978906', 'Av. Constitución #7082', 'Providencia', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '6.485.231-0', 'natural', NULL, NULL),
(332, 'Juan Vargas', 'juan.vargas@email.com', '+56929204323', 'Pasaje República #2037', 'La Serena', 'Maule', '2025-10-07', 'Contribuyente', NULL, '3.204.130-2', 'natural', NULL, NULL),
(333, 'Luis Hernández', 'luis.hernández@email.com', '+56978141136', 'Av. Libertador #8610', 'Punta Arenas', 'Valparaíso', '2025-10-07', 'Consumidor Final', NULL, '18.053.315-K', 'natural', NULL, NULL),
(334, 'Carmen Fernández', 'carmen.fernández@email.com', '+56962079619', 'Calle Libertador #2302', 'Providencia', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '15.801.121-2', 'natural', NULL, NULL),
(335, 'Carmen Rojas', 'carmen.rojas@email.com', '+56985749180', 'Pasaje Libertador #3664', 'Iquique', 'Los Lagos', '2025-10-07', 'Contribuyente', NULL, '12.358.276-4', 'natural', NULL, NULL),
(336, 'Juan Castillo', 'juan.castillo@email.com', '+56915908645', 'Calle Constitución #4258', 'Chillán', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '16.084.780-8', 'natural', NULL, NULL),
(337, 'Lorena González', 'lorena.gonzález@email.com', '+56974161222', 'Calle República #1856', 'Puerto Montt', 'Metropolitana', '2025-10-07', 'Consumidor Final', NULL, '9.484.600-5', 'natural', NULL, NULL),
(338, 'Natalia Fernández', 'natalia.fernández@email.com', '+56958973546', 'Pasaje Libertador #6365', 'Puerto Montt', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '24.486.675-1', 'natural', NULL, NULL),
(339, 'Andrés Castillo', 'andrés.castillo@email.com', '+56968018944', 'Calle República #9220', 'Concepción', 'Los Lagos', '2025-10-07', 'Contribuyente', NULL, '11.920.065-2', 'natural', NULL, NULL),
(340, 'Javiera Tapia', 'javiera.tapia@email.com', '+56986293255', 'Calle Independencia #727', 'Puerto Montt', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '7.756.351-2', 'natural', NULL, NULL),
(341, 'Carmen Pérez', 'carmen.pérez@email.com', '+56946301211', 'Av. Libertador #2449', 'Antofagasta', 'Maule', '2025-10-07', 'Contribuyente', NULL, '7.118.267-3', 'natural', NULL, NULL),
(342, 'Gonzalo Reyes', 'gonzalo.reyes@email.com', '+56999145994', 'Av. Libertador #4682', 'Valparaíso', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '24.049.948-7', 'natural', NULL, NULL),
(343, 'Andrés Araya', 'andrés.araya@email.com', '+56928346097', 'Av. Constitución #9302', 'Concepción', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '11.613.239-7', 'natural', NULL, NULL),
(344, 'Héctor Gómez', 'héctor.gómez@email.com', '+56982276409', 'Pasaje Libertador #4889', 'Viña del Mar', 'Araucanía', '2025-10-07', 'Empresa', NULL, '14.949.709-9', 'natural', NULL, NULL),
(345, 'Cristian Araya', 'cristian.araya@email.com', '+56935625695', 'Calle República #8771', 'Iquique', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '13.013.629-K', 'natural', NULL, NULL),
(346, 'Luis Reyes', 'luis.reyes@email.com', '+56991691128', 'Av. República #8011', 'Providencia', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '5.639.578-4', 'natural', NULL, NULL),
(347, 'Francisco Espinoza', 'francisco.espinoza@email.com', '+56913527071', 'Av. República #1390', 'Valparaíso', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '14.527.346-3', 'natural', NULL, NULL),
(348, 'Claudia Castro', 'claudia.castro@email.com', '+56947402533', 'Pasaje Independencia #134', 'Antofagasta', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '20.066.333-0', 'natural', NULL, NULL),
(349, 'Luis Sánchez', 'luis.sánchez@email.com', '+56939317997', 'Pasaje Constitución #903', 'Puente Alto', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '20.510.338-4', 'natural', NULL, NULL),
(350, 'Alejandro Reyes', 'alejandro.reyes@email.com', '+56942375060', 'Pasaje Independencia #742', 'Osorno', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '10.003.029-2', 'natural', NULL, NULL),
(351, 'Ana Gutiérrez', 'ana.gutiérrez@email.com', '+56983818488', 'Av. Independencia #689', 'La Florida', 'Maule', '2025-10-07', 'Contribuyente', NULL, '3.360.622-2', 'natural', NULL, NULL),
(352, 'Sandra Martínez', 'sandra.martínez@email.com', '+56953715200', 'Calle Independencia #4038', 'Iquique', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '11.293.889-3', 'natural', NULL, NULL),
(353, 'Carmen Castro', 'carmen.castro@email.com', '+56975822967', 'Calle Independencia #963', 'Concepción', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '15.794.319-7', 'natural', NULL, NULL),
(354, 'Luis Cortés', 'luis.cortés@email.com', '+56930334047', 'Calle República #6003', 'Viña del Mar', 'Metropolitana', '2025-10-07', 'Consumidor Final', NULL, '2.037.975-8', 'natural', NULL, NULL),
(355, 'Claudia Ramírez', 'claudia.ramírez@email.com', '+56932297632', 'Pasaje Independencia #5428', 'Osorno', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '2.637.642-4', 'natural', NULL, NULL),
(356, 'Carmen Morales', 'carmen.morales@email.com', '+56918075519', 'Calle Libertador #3162', 'Temuco', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '23.259.471-3', 'natural', NULL, NULL),
(357, 'Sandra Castro', 'sandra.castro@email.com', '+56981655198', 'Calle Constitución #6049', 'Puerto Montt', 'Araucanía', '2025-10-07', 'Consumidor Final', NULL, '9.440.756-7', 'natural', NULL, NULL),
(358, 'Laura Reyes', 'laura.reyes@email.com', '+56942478953', 'Calle Constitución #3551', 'Iquique', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '22.237.217-8', 'natural', NULL, NULL),
(359, 'Cristian Sepúlveda', 'cristian.sepúlveda@email.com', '+56983491070', 'Pasaje República #9174', 'La Serena', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '17.473.300-7', 'natural', NULL, NULL),
(360, 'Claudia Vargas', 'claudia.vargas@email.com', '+56924424581', 'Calle Libertador #3597', 'San Bernardo', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '16.494.821-8', 'natural', NULL, NULL),
(361, 'Sandra Gutiérrez', 'sandra.gutiérrez@email.com', '+56911748302', 'Calle Constitución #4268', 'La Serena', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '17.007.394-0', 'natural', NULL, NULL),
(362, 'Diego Fernández', 'diego.fernández@email.com', '+56981700731', 'Av. República #5948', 'Ñuñoa', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '15.405.815-K', 'natural', NULL, NULL),
(363, 'Katherine Silva', 'katherine.silva@email.com', '+56945527592', 'Av. República #1953', 'Las Condes', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '10.971.664-2', 'natural', NULL, NULL),
(364, 'Diego Flores', 'diego.flores@email.com', '+56915036040', 'Pasaje Libertador #3830', 'Las Condes', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '22.973.424-5', 'natural', NULL, NULL),
(365, 'Lorena Gutiérrez', 'lorena.gutiérrez@email.com', '+56997093310', 'Av. República #4591', 'Arica', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '19.445.815-0', 'natural', NULL, NULL),
(366, 'Claudia Vargas', 'claudia.vargas@email.com', '+56933165068', 'Calle Constitución #9956', 'Arica', 'Ñuble', '2025-10-07', 'Consumidor Final', NULL, '15.799.672-K', 'natural', NULL, NULL),
(367, 'Gonzalo Núñez', 'gonzalo.núñez@email.com', '+56926741265', 'Pasaje Independencia #1326', 'Puerto Montt', 'Araucanía', '2025-10-07', 'Consumidor Final', NULL, '8.734.613-7', 'natural', NULL, NULL),
(368, 'Carmen Castillo', 'carmen.castillo@email.com', '+56954522689', 'Av. Constitución #7168', 'Rancagua', 'Biobío', '2025-10-07', 'Empresa', NULL, '16.338.067-6', 'natural', NULL, NULL),
(369, 'Diego Fernández', 'diego.fernández@email.com', '+56947076953', 'Calle República #2791', 'Puente Alto', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '24.057.556-6', 'natural', NULL, NULL),
(370, 'Jorge Núñez', 'jorge.núñez@email.com', '+56943174477', 'Pasaje Libertador #3226', 'La Florida', 'Los Lagos', '2025-10-07', 'Contribuyente', NULL, '23.888.753-4', 'natural', NULL, NULL),
(371, 'Valentina Fernández', 'valentina.fernández@email.com', '+56920706912', 'Calle Independencia #760', 'Puerto Montt', 'Arica y Parinacota', '2025-10-07', 'Empresa', NULL, '17.582.878-8', 'natural', NULL, NULL),
(372, 'Héctor Vargas', 'héctor.vargas@email.com', '+56933004319', 'Calle Independencia #1072', 'Viña del Mar', 'Biobío', '2025-10-07', 'Empresa', NULL, '18.293.876-9', 'natural', NULL, NULL),
(373, 'Francisco Vargas', 'francisco.vargas@email.com', '+56939316676', 'Calle Independencia #193', 'Ñuñoa', 'Arica y Parinacota', '2025-10-07', 'Empresa', NULL, '10.118.629-6', 'natural', NULL, NULL),
(374, 'Fernando Reyes', 'fernando.reyes@email.com', '+56935911020', 'Pasaje Constitución #7888', 'Ñuñoa', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '3.250.499-K', 'natural', NULL, NULL),
(375, 'Carmen Contreras', 'carmen.contreras@email.com', '+56926539866', 'Calle Independencia #6971', 'Providencia', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '7.671.611-0', 'natural', NULL, NULL),
(376, 'Alejandro Rojas', 'alejandro.rojas@email.com', '+56942867536', 'Av. Independencia #1964', 'Ñuñoa', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '6.959.741-6', 'natural', NULL, NULL),
(377, 'Alejandro Carrasco', 'alejandro.carrasco@email.com', '+56952334071', 'Pasaje Constitución #1867', 'Ñuñoa', 'Araucanía', '2025-10-07', 'Empresa', NULL, '10.379.528-1', 'natural', NULL, NULL),
(378, 'Javiera Carrasco', 'javiera.carrasco@email.com', '+56981348166', 'Calle Libertador #2580', 'Ñuñoa', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '14.393.705-4', 'natural', NULL, NULL),
(379, 'Claudia Sepúlveda', 'claudia.sepúlveda@email.com', '+56979007060', 'Pasaje Independencia #365', 'Puerto Montt', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '20.042.437-9', 'natural', NULL, NULL),
(380, 'Natalia Rojas', 'natalia.rojas@email.com', '+56959745232', 'Av. Libertador #1363', 'Temuco', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '12.901.000-2', 'natural', NULL, NULL),
(381, 'Carmen Fuentes', 'carmen.fuentes@email.com', '+56961927416', 'Pasaje República #4286', 'Arica', 'Ñuble', '2025-10-07', 'Consumidor Final', NULL, '17.917.642-4', 'natural', NULL, NULL),
(382, 'Daniel Vera', 'daniel.vera@email.com', '+56910099521', 'Pasaje Independencia #6558', 'Santiago', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '2.396.220-9', 'natural', NULL, NULL),
(383, 'Katherine Rojas', 'katherine.rojas@email.com', '+56917446012', 'Pasaje Libertador #5094', 'Iquique', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '6.174.895-4', 'natural', NULL, NULL),
(384, 'José Gómez', 'josé.gómez@email.com', '+56993384990', 'Calle Independencia #2911', 'Temuco', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '14.312.444-4', 'natural', NULL, NULL),
(385, 'Sandra Sánchez', 'sandra.sánchez@email.com', '+56961475346', 'Pasaje Independencia #9541', 'Osorno', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '22.770.650-3', 'natural', NULL, NULL),
(386, 'Javiera Jiménez', 'javiera.jiménez@email.com', '+56995283259', 'Pasaje República #4653', 'Las Condes', 'Arica y Parinacota', '2025-10-07', 'Empresa', NULL, '11.170.687-5', 'natural', NULL, NULL),
(387, 'Antonio Carrasco', 'antonio.carrasco@email.com', '+56930087378', 'Calle República #1332', 'Viña del Mar', 'Biobío', '2025-10-07', 'Empresa', NULL, '12.027.007-9', 'natural', NULL, NULL),
(388, 'Elena Rojas', 'elena.rojas@email.com', '+56914799446', 'Av. República #9421', 'Chillán', 'Araucanía', '2025-10-07', 'Empresa', NULL, '12.183.165-1', 'natural', NULL, NULL),
(389, 'Ignacio Rojas', 'ignacio.rojas@email.com', '+56925296659', 'Av. República #8962', 'La Florida', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '7.447.955-3', 'natural', NULL, NULL),
(390, 'Sofía Álvarez', 'sofía.álvarez@email.com', '+56997327663', 'Pasaje República #6309', 'Puerto Montt', 'Araucanía', '2025-10-07', 'Consumidor Final', NULL, '11.085.282-7', 'natural', NULL, NULL),
(391, 'Patricia Fernández', 'patricia.fernández@email.com', '+56976291270', 'Pasaje Libertador #1739', 'Valparaíso', 'Biobío', '2025-10-07', 'Empresa', NULL, '4.952.021-2', 'natural', NULL, NULL),
(392, 'Javiera Vargas', 'javiera.vargas@email.com', '+56917648901', 'Calle Libertador #211', 'Temuco', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '8.053.226-1', 'natural', NULL, NULL),
(393, 'Juan Sánchez', 'juan.sánchez@email.com', '+56972070131', 'Calle República #5284', 'Coquimbo', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '4.740.239-5', 'natural', NULL, NULL),
(394, 'Sandra Rodríguez', 'sandra.rodríguez@email.com', '+56997893537', 'Pasaje Independencia #7125', 'Valparaíso', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '14.128.281-6', 'natural', NULL, NULL),
(395, 'Francisca Vásquez', 'francisca.vásquez@email.com', '+56975271228', 'Av. República #8401', 'Providencia', 'Araucanía', '2025-10-07', 'Empresa', NULL, '2.105.665-0', 'natural', NULL, NULL),
(396, 'Lorena Flores', 'lorena.flores@email.com', '+56962465828', 'Pasaje República #893', 'Puente Alto', 'Maule', '2025-10-07', 'Empresa', NULL, '8.990.114-6', 'natural', NULL, NULL),
(397, 'Francisca Jiménez', 'francisca.jiménez@email.com', '+56972556127', 'Pasaje Libertador #7054', 'Punta Arenas', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '13.315.401-9', 'natural', NULL, NULL),
(398, 'Javiera Tapia', 'javiera.tapia@email.com', '+56964280947', 'Av. Constitución #1903', 'Coquimbo', 'Coquimbo', '2025-10-07', 'Empresa', NULL, '20.983.002-7', 'natural', NULL, NULL),
(399, 'José Gómez', 'josé.gómez@email.com', '+56988870213', 'Calle Libertador #3802', 'Puente Alto', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '15.584.585-6', 'natural', NULL, NULL),
(400, 'Gonzalo Torres', 'gonzalo.torres@email.com', '+56955142108', 'Calle Constitución #185', 'Puerto Montt', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '12.834.121-8', 'natural', NULL, NULL),
(401, 'Cristian Rojas', 'cristian.rojas@email.com', '+56961051572', 'Pasaje Libertador #7481', 'Coquimbo', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '24.078.535-8', 'natural', NULL, NULL),
(402, 'Diego González', 'diego.gonzález@email.com', '+56996459875', 'Calle Libertador #9820', 'Viña del Mar', 'O\'Higgins', '2025-10-07', 'Empresa', NULL, '5.833.529-0', 'natural', NULL, NULL),
(403, 'Javiera Sánchez', 'javiera.sánchez@email.com', '+56944340809', 'Calle Independencia #3900', 'San Bernardo', 'Maule', '2025-10-07', 'Empresa', NULL, '19.077.868-1', 'natural', NULL, NULL),
(404, 'Katherine Pérez', 'katherine.pérez@email.com', '+56925331163', 'Pasaje República #5206', 'Santiago', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '23.662.778-0', 'natural', NULL, NULL),
(405, 'Rosa Moreno', 'rosa.moreno@email.com', '+56951033127', 'Calle Libertador #8088', 'San Bernardo', 'Biobío', '2025-10-07', 'Empresa', NULL, '21.871.574-5', 'natural', NULL, NULL),
(406, 'Sandra Martínez', 'sandra.martínez@email.com', '+56971619418', 'Av. Libertador #6961', 'Chillán', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '24.464.981-5', 'natural', NULL, NULL),
(407, 'Katherine Vásquez', 'katherine.vásquez@email.com', '+56930970242', 'Av. República #2032', 'Concepción', 'Biobío', '2025-10-07', 'Contribuyente', NULL, '6.905.002-6', 'natural', NULL, NULL),
(408, 'Paula Jiménez', 'paula.jiménez@email.com', '+56997855864', 'Av. República #5374', 'La Florida', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '9.826.952-5', 'natural', NULL, NULL),
(409, 'Fernando Castillo', 'fernando.castillo@email.com', '+56942382357', 'Pasaje República #8957', 'Rancagua', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '12.457.540-0', 'natural', NULL, NULL),
(410, 'Paula Tapia', 'paula.tapia@email.com', '+56919163055', 'Pasaje República #9820', 'Chillán', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '9.847.058-1', 'natural', NULL, NULL),
(411, 'Valentina Carrasco', 'valentina.carrasco@email.com', '+56981782579', 'Pasaje República #1743', 'Chillán', 'Arica y Parinacota', '2025-10-07', 'Empresa', NULL, '22.745.978-6', 'natural', NULL, NULL),
(412, 'Valentina Tapia', 'valentina.tapia@email.com', '+56947839553', 'Calle Libertador #4737', 'Las Condes', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '18.264.987-2', 'natural', NULL, NULL),
(413, 'Héctor Herrera', 'héctor.herrera@email.com', '+56934782276', 'Pasaje República #5412', 'Puerto Montt', 'Coquimbo', '2025-10-07', 'Empresa', NULL, '23.796.827-1', 'natural', NULL, NULL),
(414, 'Javiera Silva', 'javiera.silva@email.com', '+56927183708', 'Av. Constitución #2135', 'Santiago', 'Maule', '2025-10-07', 'Empresa', NULL, '6.030.210-3', 'natural', NULL, NULL),
(415, 'Ignacio Hernández', 'ignacio.hernández@email.com', '+56962762259', 'Calle República #8039', 'La Serena', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '13.822.951-3', 'natural', NULL, NULL),
(416, 'Valentina Morales', 'valentina.morales@email.com', '+56919727795', 'Av. Independencia #4562', 'Iquique', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '19.843.767-0', 'natural', NULL, NULL),
(417, 'Javiera Vargas', 'javiera.vargas@email.com', '+56986697258', 'Pasaje Libertador #3692', 'Rancagua', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '8.199.563-K', 'natural', NULL, NULL),
(418, 'María Muñoz', 'maría.muñoz@email.com', '+56959570641', 'Av. Independencia #9522', 'Osorno', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '24.091.048-9', 'natural', NULL, NULL),
(419, 'Luis Ramírez', 'luis.ramírez@email.com', '+56955825023', 'Pasaje Constitución #1850', 'San Bernardo', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '18.063.423-1', 'natural', NULL, NULL),
(420, 'Claudia Tapia', 'claudia.tapia@email.com', '+56946814163', 'Pasaje Constitución #7570', 'Chillán', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '5.586.951-0', 'natural', NULL, NULL),
(421, 'Laura Vásquez', 'laura.vásquez@email.com', '+56977745315', 'Calle República #3007', 'Talca', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '20.218.607-6', 'natural', NULL, NULL),
(422, 'Manuel Flores', 'manuel.flores@email.com', '+56992233432', 'Calle República #2776', 'Concepción', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '9.598.480-0', 'natural', NULL, NULL),
(423, 'Gonzalo Araya', 'gonzalo.araya@email.com', '+56930177032', 'Calle República #9363', 'Chillán', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '9.513.712-1', 'natural', NULL, NULL),
(424, 'Laura Jiménez', 'laura.jiménez@email.com', '+56972308083', 'Pasaje República #9281', 'Viña del Mar', 'Maule', '2025-10-07', 'Empresa', NULL, '22.797.269-6', 'natural', NULL, NULL),
(425, 'Katherine Torres', 'katherine.torres@email.com', '+56928561537', 'Calle Constitución #6677', 'Rancagua', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '12.864.290-0', 'natural', NULL, NULL),
(426, 'Daniel González', 'daniel.gonzález@email.com', '+56978774154', 'Pasaje Libertador #850', 'Viña del Mar', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '6.224.055-5', 'natural', NULL, NULL),
(427, 'Gonzalo Carrasco', 'gonzalo.carrasco@email.com', '+56999987638', 'Av. Independencia #8114', 'Viña del Mar', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '9.677.902-K', 'natural', NULL, NULL),
(428, 'Fernando Tapia', 'fernando.tapia@email.com', '+56924480671', 'Pasaje Libertador #4400', 'La Serena', 'Tarapacá', '2025-10-07', 'Contribuyente', NULL, '15.034.826-9', 'natural', NULL, NULL),
(429, 'Francisco Vera', 'francisco.vera@email.com', '+56923127055', 'Calle República #4324', 'Providencia', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '23.009.197-8', 'natural', NULL, NULL),
(430, 'Javier Álvarez', 'javier.álvarez@email.com', '+56993047655', 'Av. Independencia #4556', 'Talca', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '18.228.123-9', 'natural', NULL, NULL),
(431, 'Juan Contreras', 'juan.contreras@email.com', '+56963116197', 'Av. República #7376', 'San Bernardo', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '3.555.257-K', 'natural', NULL, NULL),
(432, 'Francisca Morales', 'francisca.morales@email.com', '+56958489578', 'Calle Constitución #1447', 'Iquique', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '19.884.159-5', 'natural', NULL, NULL),
(433, 'Manuel Carrasco', 'manuel.carrasco@email.com', '+56911219094', 'Av. Libertador #9059', 'Ñuñoa', 'Tarapacá', '2025-10-07', 'Consumidor Final', NULL, '23.856.265-1', 'natural', NULL, NULL),
(434, 'Diego González', 'diego.gonzález@email.com', '+56952389889', 'Calle Libertador #1373', 'Temuco', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '17.330.719-5', 'natural', NULL, NULL),
(435, 'Luis Castro', 'luis.castro@email.com', '+56969914730', 'Pasaje Independencia #5449', 'Talca', 'Tarapacá', '2025-10-07', 'Empresa', NULL, '3.388.310-2', 'natural', NULL, NULL),
(436, 'Javier Morales', 'javier.morales@email.com', '+56922358622', 'Pasaje República #9679', 'Arica', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '9.530.764-7', 'natural', NULL, NULL),
(437, 'Gonzalo Vargas', 'gonzalo.vargas@email.com', '+56996840661', 'Calle Constitución #2133', 'La Serena', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '22.567.771-9', 'natural', NULL, NULL),
(438, 'Carmen Moreno', 'carmen.moreno@email.com', '+56910007122', 'Pasaje República #5468', 'Concepción', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '7.375.310-4', 'natural', NULL, NULL),
(439, 'Manuel Vargas', 'manuel.vargas@email.com', '+56998118303', 'Av. Constitución #7671', 'Maipú', 'Maule', '2025-10-07', 'Consumidor Final', NULL, '11.888.563-5', 'natural', NULL, NULL),
(440, 'Lorena Pérez', 'lorena.pérez@email.com', '+56934263926', 'Calle Independencia #3592', 'Chillán', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '21.394.500-9', 'natural', NULL, NULL),
(441, 'Andrés Moreno', 'andrés.moreno@email.com', '+56913110623', 'Calle Independencia #7963', 'Rancagua', 'Biobío', '2025-10-07', 'Empresa', NULL, '19.976.242-7', 'natural', NULL, NULL),
(442, 'Francisco Cortés', 'francisco.cortés@email.com', '+56939419144', 'Calle República #3639', 'Providencia', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '6.584.203-3', 'natural', NULL, NULL),
(443, 'Carlos Vásquez', 'carlos.vásquez@email.com', '+56938360377', 'Av. República #5827', 'La Florida', 'Araucanía', '2025-10-07', 'Consumidor Final', NULL, '23.328.572-2', 'natural', NULL, NULL),
(444, 'Cristian Hernández', 'cristian.hernández@email.com', '+56912036641', 'Pasaje Independencia #3078', 'Maipú', 'Maule', '2025-10-07', 'Contribuyente', NULL, '12.960.981-8', 'natural', NULL, NULL),
(445, 'Rosa Valenzuela', 'rosa.valenzuela@email.com', '+56918964108', 'Calle Libertador #4340', 'Coquimbo', 'Los Lagos', '2025-10-07', 'Contribuyente', NULL, '19.275.940-4', 'natural', NULL, NULL),
(446, 'Paula Gutiérrez', 'paula.gutiérrez@email.com', '+56924956551', 'Pasaje República #8534', 'Puente Alto', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '21.197.259-9', 'natural', NULL, NULL),
(447, 'Fernando Torres', 'fernando.torres@email.com', '+56967052710', 'Av. Constitución #1209', 'Iquique', 'Arica y Parinacota', '2025-10-07', 'Contribuyente', NULL, '14.403.833-9', 'natural', NULL, NULL),
(448, 'Carlos González', 'carlos.gonzález@email.com', '+56987640200', 'Calle Libertador #309', 'Chillán', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '21.592.939-6', 'natural', NULL, NULL),
(449, 'Natalia Castillo', 'natalia.castillo@email.com', '+56933892740', 'Pasaje Constitución #2123', 'Concepción', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '3.280.665-1', 'natural', NULL, NULL),
(450, 'Cristian Hernández', 'cristian.hernández@email.com', '+56995506830', 'Pasaje Constitución #362', 'Concepción', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '10.242.602-9', 'natural', NULL, NULL),
(451, 'Ignacio Torres', 'ignacio.torres@email.com', '+56915649574', 'Calle Independencia #8701', 'Chillán', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '15.267.910-6', 'natural', NULL, NULL),
(452, 'Paula Pérez', 'paula.pérez@email.com', '+56922839928', 'Calle Constitución #5554', 'Iquique', 'Coquimbo', '2025-10-07', 'Empresa', NULL, '5.383.621-6', 'natural', NULL, NULL),
(453, 'Manuel Carrasco', 'manuel.carrasco@email.com', '+56931879238', 'Av. República #4909', 'San Bernardo', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '9.995.842-1', 'natural', NULL, NULL),
(454, 'Elena Reyes', 'elena.reyes@email.com', '+56962929280', 'Calle Independencia #930', 'Ñuñoa', 'Magallanes', '2025-10-07', 'Consumidor Final', NULL, '1.069.562-7', 'natural', NULL, NULL),
(455, 'Natalia Reyes', 'natalia.reyes@email.com', '+56947538578', 'Calle Constitución #935', 'Chillán', 'Metropolitana', '2025-10-07', 'Consumidor Final', NULL, '4.322.628-2', 'natural', NULL, NULL),
(456, 'Paula Reyes', 'paula.reyes@email.com', '+56963456559', 'Av. Constitución #7691', 'Providencia', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '4.434.299-5', 'natural', NULL, NULL),
(457, 'Laura Silva', 'laura.silva@email.com', '+56968610582', 'Av. Libertador #7736', 'Ñuñoa', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '7.657.454-5', 'natural', NULL, NULL),
(458, 'Héctor Carrasco', 'héctor.carrasco@email.com', '+56975403775', 'Av. República #4417', 'Osorno', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '12.685.952-K', 'natural', NULL, NULL),
(459, 'Ignacio Soto', 'ignacio.soto@email.com', '+56932602731', 'Av. Libertador #1618', 'Temuco', 'Arica y Parinacota', '2025-10-07', 'Empresa', NULL, '14.258.735-1', 'natural', NULL, NULL),
(460, 'Paula Álvarez', 'paula.álvarez@email.com', '+56974966747', 'Av. Libertador #5572', 'Valparaíso', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '3.510.735-5', 'natural', NULL, NULL),
(461, 'Katherine Gómez', 'katherine.gómez@email.com', '+56991864707', 'Pasaje Constitución #5900', 'Ñuñoa', 'Antofagasta', '2025-10-07', 'Empresa', NULL, '4.509.170-8', 'natural', NULL, NULL),
(462, 'Natalia Carrasco', 'natalia.carrasco@email.com', '+56931452658', 'Calle Libertador #3857', 'Las Condes', 'Maule', '2025-10-07', 'Empresa', NULL, '20.414.150-9', 'natural', NULL, NULL),
(463, 'Patricia Reyes', 'patricia.reyes@email.com', '+56991753159', 'Calle República #4687', 'Providencia', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '16.611.758-5', 'natural', NULL, NULL),
(464, 'Ana Gómez', 'ana.gómez@email.com', '+56999333042', 'Pasaje Libertador #8469', 'Puerto Montt', 'Biobío', '2025-10-07', 'Empresa', NULL, '4.619.119-6', 'natural', NULL, NULL),
(465, 'Elena Rojas', 'elena.rojas@email.com', '+56988778036', 'Av. Independencia #644', 'Maipú', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '1.911.092-3', 'natural', NULL, NULL),
(466, 'Ana Pérez', 'ana.pérez@email.com', '+56970266214', 'Calle República #1407', 'Chillán', 'Ñuble', '2025-10-07', 'Empresa', NULL, '20.743.153-2', 'natural', NULL, NULL),
(467, 'Jorge Silva', 'jorge.silva@email.com', '+56914394980', 'Calle Constitución #4510', 'Temuco', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '15.309.672-4', 'natural', NULL, NULL),
(468, 'María González', 'maría.gonzález@email.com', '+56946499871', 'Av. Independencia #1445', 'Antofagasta', 'Araucanía', '2025-10-07', 'Empresa', NULL, '8.793.278-8', 'natural', NULL, NULL),
(469, 'Antonio Fuentes', 'antonio.fuentes@email.com', '+56960721221', 'Calle Libertador #2917', 'Iquique', 'Valparaíso', '2025-10-07', 'Empresa', NULL, '15.449.067-1', 'natural', NULL, NULL),
(470, 'Claudia Valenzuela', 'claudia.valenzuela@email.com', '+56934441959', 'Calle Constitución #4529', 'Santiago', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '9.696.632-6', 'natural', NULL, NULL),
(471, 'Carlos Flores', 'carlos.flores@email.com', '+56982498160', 'Av. Independencia #9444', 'Concepción', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '4.538.778-K', 'natural', NULL, NULL),
(472, 'Verónica Núñez', 'verónica.núñez@email.com', '+56957353412', 'Calle Independencia #3010', 'Chillán', 'Araucanía', '2025-10-07', 'Contribuyente', NULL, '24.623.576-7', 'natural', NULL, NULL),
(473, 'María Herrera', 'maría.herrera@email.com', '+56994509965', 'Calle Libertador #334', 'Maipú', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '11.519.581-6', 'natural', NULL, NULL),
(474, 'Elena Sánchez', 'elena.sánchez@email.com', '+56977781190', 'Av. República #7883', 'Santiago', 'Metropolitana', '2025-10-07', 'Empresa', NULL, '2.613.753-5', 'natural', NULL, NULL),
(475, 'Carlos Castro', 'carlos.castro@email.com', '+56971030380', 'Av. Libertador #6172', 'Maipú', 'Metropolitana', '2025-10-07', 'Contribuyente', NULL, '7.337.674-2', 'natural', NULL, NULL),
(476, 'Lorena Valenzuela', 'lorena.valenzuela@email.com', '+56919035816', 'Av. Constitución #6271', 'Las Condes', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '6.889.275-9', 'natural', NULL, NULL),
(477, 'Carlos Castillo', 'carlos.castillo@email.com', '+56977898761', 'Av. República #1167', 'Arica', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '7.422.277-3', 'natural', NULL, NULL),
(478, 'Carlos Castillo', 'carlos.castillo@email.com', '+56925878019', 'Av. República #3329', 'San Bernardo', 'Los Lagos', '2025-10-07', 'Consumidor Final', NULL, '3.666.153-4', 'natural', NULL, NULL),
(479, 'Andrés Álvarez', 'andrés.álvarez@email.com', '+56937081304', 'Pasaje Libertador #5379', 'Osorno', 'Antofagasta', '2025-10-07', 'Contribuyente', NULL, '18.332.910-3', 'natural', NULL, NULL),
(480, 'Héctor Rojas', 'héctor.rojas@email.com', '+56971280072', 'Av. Independencia #2700', 'La Serena', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '24.937.403-2', 'natural', NULL, NULL),
(481, 'Cristian Muñoz', 'cristian.muñoz@email.com', '+56911124279', 'Pasaje Constitución #4668', 'San Bernardo', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '16.246.911-8', 'natural', NULL, NULL),
(482, 'Carmen Ramírez', 'carmen.ramírez@email.com', '+56956865268', 'Av. Libertador #2212', 'Chillán', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '18.908.209-6', 'natural', NULL, NULL),
(483, 'Marcela Muñoz', 'marcela.muñoz@email.com', '+56922804354', 'Pasaje Independencia #4198', 'Ñuñoa', 'Maule', '2025-10-07', 'Contribuyente', NULL, '20.792.562-4', 'natural', NULL, NULL),
(484, 'Gonzalo Sepúlveda', 'gonzalo.sepúlveda@email.com', '+56925845956', 'Av. República #1952', 'Talca', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '21.228.807-1', 'natural', NULL, NULL),
(485, 'Rosa Martínez', 'rosa.martínez@email.com', '+56959830188', 'Pasaje República #8236', 'Santiago', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '4.643.020-4', 'natural', NULL, NULL),
(486, 'Sandra Carrasco', 'sandra.carrasco@email.com', '+56923332946', 'Calle Libertador #6566', 'Ñuñoa', 'Magallanes', '2025-10-07', 'Empresa', NULL, '7.383.052-4', 'natural', NULL, NULL),
(487, 'Fernando Carrasco', 'fernando.carrasco@email.com', '+56996845224', 'Pasaje Constitución #1154', 'La Serena', 'Arica y Parinacota', '2025-10-07', 'Consumidor Final', NULL, '1.855.193-4', 'natural', NULL, NULL),
(488, 'Carmen Vera', 'carmen.vera@email.com', '+56996803942', 'Pasaje República #6433', 'Punta Arenas', 'Biobío', '2025-10-07', 'Empresa', NULL, '4.075.776-7', 'natural', NULL, NULL),
(489, 'Rosa Vera', 'rosa.vera@email.com', '+56960713430', 'Calle Constitución #7675', 'Maipú', 'Magallanes', '2025-10-07', 'Contribuyente', NULL, '7.408.768-K', 'natural', NULL, NULL),
(490, 'Verónica Cortés', 'verónica.cortés@email.com', '+56975188264', 'Av. Independencia #4791', 'Talca', 'O\'Higgins', '2025-10-07', 'Consumidor Final', NULL, '24.409.270-5', 'natural', NULL, NULL),
(491, 'Carmen Parra', 'carmen.parra@email.com', '+56919588300', 'Av. Constitución #4385', 'Santiago', 'Ñuble', '2025-10-07', 'Empresa', NULL, '24.020.229-8', 'natural', NULL, NULL),
(492, 'Luis Pérez', 'luis.pérez@email.com', '+56950795734', 'Av. Libertador #4348', 'Ñuñoa', 'Ñuble', '2025-10-07', 'Contribuyente', NULL, '6.183.005-7', 'natural', NULL, NULL),
(493, 'Lorena Díaz', 'lorena.díaz@email.com', '+56917665605', 'Calle Libertador #7243', 'Ñuñoa', 'Biobío', '2025-10-07', 'Consumidor Final', NULL, '20.402.658-0', 'natural', NULL, NULL),
(494, 'Diego Sepúlveda', 'diego.sepúlveda@email.com', '+56972716788', 'Calle Independencia #5386', 'Maipú', 'Coquimbo', '2025-10-07', 'Contribuyente', NULL, '22.354.675-7', 'natural', NULL, NULL),
(495, 'Natalia Parra', 'natalia.parra@email.com', '+56972480458', 'Calle Libertador #1833', 'Santiago', 'Biobío', '2025-10-07', 'Empresa', NULL, '17.829.085-1', 'natural', NULL, NULL),
(496, 'Claudia Moreno', 'claudia.moreno@email.com', '+56912480339', 'Calle Independencia #8826', 'Osorno', 'Los Lagos', '2025-10-07', 'Contribuyente', NULL, '5.433.274-2', 'natural', NULL, NULL),
(497, 'Andrés Parra', 'andrés.parra@email.com', '+56985485517', 'Calle República #7657', 'Talca', 'Ñuble', '2025-10-07', 'Empresa', NULL, '23.475.891-8', 'natural', NULL, NULL),
(498, 'Gabriel Martínez', 'gabriel.martínez@email.com', '+56979144458', 'Pasaje República #6739', 'La Florida', 'O\'Higgins', '2025-10-07', 'Contribuyente', NULL, '17.474.695-8', 'natural', NULL, NULL),
(499, 'Lorena Sánchez', 'lorena.sánchez@email.com', '+56950844709', 'Calle Libertador #9362', 'Coquimbo', 'Los Lagos', '2025-10-07', 'Contribuyente', NULL, '22.351.988-1', 'natural', NULL, NULL),
(500, 'Sandra Gutiérrez', 'sandra.gutiérrez@email.com', '+56963717561', 'Av. Constitución #4793', 'Rancagua', 'Araucanía', '2025-10-07', 'Empresa', NULL, '12.217.643-6', 'natural', NULL, NULL),
(501, 'Isabel González', 'isabel.gonzález@email.com', '+56927524594', 'Pasaje Libertador #8268', 'Puente Alto', 'Valparaíso', '2025-10-07', 'Contribuyente', NULL, '10.755.415-7', 'natural', NULL, NULL),
(502, 'Antonio Vargas', 'antonio.vargas@email.com', '+56934322325', 'Av. República #5766', 'Coquimbo', 'Coquimbo', '2025-10-07', 'Consumidor Final', NULL, '5.071.421-7', 'natural', NULL, NULL),
(503, 'Cristian Fuentes', 'cristian.fuentes@email.com', '+56967185488', 'Pasaje Independencia #4271', 'Talca', 'Los Lagos', '2025-10-07', 'Empresa', NULL, '16.447.561-1', 'natural', NULL, NULL),
(504, 'Ana Núñez', 'ana.núñez@email.com', '+56978320834', 'Calle República #1580', 'Chillán', 'Antofagasta', '2025-10-07', 'Consumidor Final', NULL, '15.633.487-1', 'natural', NULL, NULL),
(505, 'Ana Martín', 'ana@email.com', '+56955666777', 'Av. Sur 321', 'Ñuñoa', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '55.666.777-8', 'natural', NULL, NULL),
(506, 'Luis Sánchez', 'luis@email.com', '+56999888777', 'Calle Este 654', 'Maipú', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '99.888.777-6', 'natural', NULL, NULL),
(507, 'Roberto Silva', 'roberto@email.com', '+56912345678', 'Av. Libertador 123', 'Santiago', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '13.456.789-0', 'natural', NULL, NULL),
(508, 'Patricia Torres', 'patricia@email.com', '+56923456789', 'Calle Independencia 456', 'Las Condes', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '14.567.890-1', 'natural', NULL, NULL),
(509, 'Miguel Herrera', 'miguel@email.com', '+56934567890', 'Pasaje República 789', 'Providencia', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '15.678.901-2', 'natural', NULL, NULL),
(510, 'Isabel Morales', 'isabel@email.com', '+56945678901', 'Av. Constitución 321', 'Ñuñoa', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '16.789.012-3', 'natural', NULL, NULL),
(511, 'Fernando Castro', 'fernando@email.com', '+56956789012', 'Calle Norte 654', 'Maipú', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '17.890.123-4', 'natural', NULL, NULL),
(512, 'Carlos López', 'carlos.lopez@email.com', '+56911223344', '', 'Santiago', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '', 'natural', NULL, NULL),
(514, 'Laura Sánchez', 'laura.sanchez@email.com', '+56944332211', 'Dirección de prueba', 'Santiago', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '44.333.222-1', 'natural', NULL, NULL);
INSERT INTO `djangoVerVictorMondaca_clientes` (`id`, `nombre`, `email`, `telefono`, `direccion`, `comuna`, `region`, `fecha_registro`, `tipo_cliente`, `observaciones`, `rut`, `tipo_persona`, `giro`, `contacto`) VALUES
(515, 'Miguel Torres', 'miguel.torres@email.com', '+56977889900', 'Dirección de prueba', 'Santiago', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '77.889.900-3', 'natural', NULL, NULL),
(516, 'Cliente General', 'general@bazar.com', '+56900000000', 'Dirección de prueba', 'Santiago', 'Metropolitana', '2025-10-07', 'consumidor_final', NULL, '00.000.000-0', 'natural', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `djangoVerVictorMondaca_productos`
--

CREATE TABLE `djangoVerVictorMondaca_productos` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
  `categoria` varchar(50) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `observaciones` longtext DEFAULT NULL,
  `proveedor` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `djangoVerVictorMondaca_productos`
--

INSERT INTO `djangoVerVictorMondaca_productos` (`id`, `nombre`, `descripcion`, `precio`, `stock`, `categoria`, `estado`, `observaciones`, `proveedor`) VALUES
(1, 'Coca Cola 500ml', 'Bebida gaseosa', 1200.00, 50, 'Bebidas', 'disponible', NULL, 'Proveedor Local'),
(2, 'Agua Mineral 1L', 'Agua purificada', 800.00, 30, 'Bebidas', 'disponible', NULL, 'Proveedor Local'),
(3, 'Jugo de Naranja 1L', 'Jugo natural', 1000.00, 40, 'Bebidas', 'disponible', NULL, 'Proveedor Local'),
(4, 'Cerveza 350ml', 'Cerveza nacional', 1500.00, 25, 'Bebidas', 'disponible', NULL, 'Proveedor Local'),
(5, 'Vino Tinto 750ml', 'Vino de mesa', 3000.00, 15, 'Bebidas', 'disponible', NULL, 'Proveedor Local'),
(6, 'Pan de Molde', 'Pan blanco', 1200.00, 30, 'Panadería', 'disponible', NULL, 'Proveedor Local'),
(7, 'Galletas Saladas', 'Galletas de agua', 800.00, 20, 'Panadería', 'disponible', NULL, 'Proveedor Local'),
(8, 'Tortillas', 'Tortillas de harina', 1500.00, 25, 'Panadería', 'disponible', NULL, 'Proveedor Local'),
(9, 'Pan', 'Producto fresco de panadería', 1200.00, 30, 'Panadería', 'disponible', NULL, 'Proveedor Local'),
(10, 'Leche', 'Producto fresco de lácteos', 1000.00, 25, 'Lácteos', 'disponible', NULL, 'Proveedor Local'),
(11, 'Energizante 250ml', 'Bebida energética', 2000.00, 20, 'Bebidas', 'disponible', NULL, 'Proveedor Norte'),
(12, 'Té en Bolsitas', 'Té negro', 500.00, 30, 'Bebidas', 'disponible', NULL, 'Proveedor Norte'),
(13, 'Chocolate en Polvo', 'Cacao en polvo', 1800.00, 25, 'Bebidas', 'disponible', NULL, 'Proveedor Norte'),
(14, 'Agua Saborizada', 'Agua con sabor', 1000.00, 20, 'Bebidas', 'disponible', NULL, 'Proveedor Norte'),
(15, 'Arroz 1kg', 'Arroz grano largo', 1200.00, 20, 'Granos', 'disponible', NULL, 'Proveedor Central'),
(16, 'Fideos', 'Fideos largos', 800.00, 30, 'Granos', 'disponible', NULL, 'Proveedor Central'),
(17, 'Azúcar 1kg', 'Azúcar blanca', 1000.00, 15, 'Endulzantes', 'disponible', NULL, 'Proveedor Central'),
(18, 'Sal 500g', 'Sal marina', 300.00, 20, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(19, 'Aceite 1L', 'Aceite vegetal', 2500.00, 10, 'Aceites', 'disponible', NULL, 'Proveedor Central'),
(20, 'Leche 1L', 'Leche entera', 800.00, 25, 'Lácteos', 'disponible', NULL, 'Proveedor Lácteos'),
(21, 'Huevos x12', 'Huevos frescos', 1200.00, 20, 'Lácteos', 'disponible', NULL, 'Proveedor Lácteos'),
(22, 'Queso 200g', 'Queso gouda', 2000.00, 15, 'Lácteos', 'disponible', NULL, 'Proveedor Lácteos'),
(23, 'Jamón 200g', 'Jamón cocido', 1800.00, 12, 'Carnes', 'disponible', NULL, 'Proveedor Carnes'),
(24, 'Aceitunas', 'Aceitunas verdes', 1500.00, 20, 'Conservas', 'disponible', NULL, 'Proveedor Sur'),
(25, 'Atún', 'Atún en lata', 2000.00, 15, 'Conservas', 'disponible', NULL, 'Proveedor Sur'),
(26, 'Café', 'Café molido 500g', 3000.00, 10, 'Bebidas', 'disponible', NULL, 'Proveedor Central'),
(27, 'Té', 'Té negro 100 bolsas', 2500.00, 8, 'Bebidas', 'disponible', NULL, 'Proveedor Central'),
(28, 'Galletas', 'Galletas surtidas', 1200.00, 25, 'Dulces', 'disponible', NULL, 'Proveedor Central'),
(29, 'Yogurt', 'Yogurt natural', 800.00, 30, 'Lácteos', 'disponible', NULL, 'Proveedor Lácteos'),
(30, 'Mantequilla', 'Mantequilla 200g', 1500.00, 20, 'Lácteos', 'disponible', NULL, 'Proveedor Lácteos'),
(31, 'Cereal', 'Cereal de avena', 2500.00, 15, 'Cereales', 'disponible', NULL, 'Proveedor Central'),
(32, 'Miel', 'Miel natural 500g', 3000.00, 10, 'Endulzantes', 'disponible', NULL, 'Proveedor Central'),
(33, 'Vinagre', 'Vinagre blanco 500ml', 800.00, 25, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(34, 'Detergente', 'Detergente líquido 1L', 2000.00, 20, 'Limpieza', 'disponible', NULL, 'Proveedor Norte'),
(35, 'Shampoo', 'Shampoo 400ml', 1800.00, 15, 'Higiene', 'disponible', NULL, 'Proveedor Norte'),
(36, 'Jabón', 'Jabón en barra', 1600.00, 18, 'Higiene', 'disponible', NULL, 'Proveedor Norte'),
(37, 'Papel Higiénico', 'Papel higiénico 4 rollos', 2500.00, 12, 'Higiene', 'disponible', NULL, 'Proveedor Norte'),
(38, 'Toallas de Papel', 'Toallas de papel absorbentes', 3000.00, 8, 'Higiene', 'disponible', NULL, 'Proveedor Norte'),
(39, 'Cloro', 'Cloro desinfectante 1L', 1200.00, 15, 'Limpieza', 'disponible', NULL, 'Proveedor Sur'),
(40, 'Esponja', 'Esponjas para lavar', 1000.00, 20, 'Limpieza', 'disponible', NULL, 'Proveedor Sur'),
(41, 'Servilletas', 'Servilletas de papel', 1500.00, 18, 'Desechables', 'disponible', NULL, 'Proveedor Sur'),
(42, 'Bolsas Basura', 'Bolsas para basura', 2000.00, 12, 'Desechables', 'disponible', NULL, 'Proveedor Sur'),
(43, 'Desodorante', 'Desodorante en spray', 1800.00, 10, 'Higiene', 'disponible', NULL, 'Proveedor Sur'),
(44, 'Quinoa', 'Quinoa orgánica', 4000.00, 8, 'Granos', 'disponible', NULL, 'Proveedor Central'),
(45, 'Avena', 'Avena en hojuelas', 1500.00, 15, 'Granos', 'disponible', NULL, 'Proveedor Central'),
(46, 'Lentejas', 'Lentejas secas', 2000.00, 12, 'Granos', 'disponible', NULL, 'Proveedor Central'),
(47, 'Porotos', 'Porotos secos', 1800.00, 10, 'Granos', 'disponible', NULL, 'Proveedor Central'),
(48, 'Garbanzos', 'Garbanzos secos', 2200.00, 8, 'Granos', 'disponible', NULL, 'Proveedor Central'),
(49, 'Trigo', 'Trigo para moler', 1000.00, 15, 'Granos', 'disponible', NULL, 'Proveedor Central'),
(50, 'Cebada', 'Cebada perlada', 1600.00, 10, 'Granos', 'disponible', NULL, 'Proveedor Central'),
(51, 'Maíz', 'Maíz en grano', 1400.00, 12, 'Granos', 'disponible', NULL, 'Proveedor Central'),
(52, 'Crema', 'Crema para cocinar', 1200.00, 15, 'Lácteos', 'disponible', NULL, 'Proveedor Lácteos'),
(53, 'Ricotta', 'Ricotta fresca', 1800.00, 10, 'Lácteos', 'disponible', NULL, 'Proveedor Lácteos'),
(54, 'Mozzarella', 'Mozzarella fresca', 2500.00, 12, 'Lácteos', 'disponible', NULL, 'Proveedor Lácteos'),
(55, 'Parmesano', 'Parmesano rallado', 3000.00, 8, 'Lácteos', 'disponible', NULL, 'Proveedor Lácteos'),
(56, 'Cottage', 'Queso cottage', 1600.00, 10, 'Lácteos', 'disponible', NULL, 'Proveedor Lácteos'),
(57, 'Salchichas', 'Salchichas vienesas', 1500.00, 15, 'Carnes', 'disponible', NULL, 'Proveedor Carnes'),
(58, 'Pollo', 'Pollo entero', 3000.00, 8, 'Carnes', 'disponible', NULL, 'Proveedor Carnes'),
(59, 'Carne Molida', 'Carne molida fresca', 4000.00, 6, 'Carnes', 'disponible', NULL, 'Proveedor Carnes'),
(60, 'Pescado', 'Pescado fresco', 3500.00, 5, 'Carnes', 'disponible', NULL, 'Proveedor Carnes'),
(61, 'Tocino', 'Tocino ahumado', 2500.00, 8, 'Carnes', 'disponible', NULL, 'Proveedor Carnes'),
(62, 'Chorizo', 'Chorizo parrillero', 2000.00, 10, 'Carnes', 'disponible', NULL, 'Proveedor Carnes'),
(63, 'Longaniza', 'Longaniza fresca', 2200.00, 8, 'Carnes', 'disponible', NULL, 'Proveedor Carnes'),
(64, 'Pechuga', 'Pechuga de pollo', 2800.00, 10, 'Carnes', 'disponible', NULL, 'Proveedor Carnes'),
(65, 'Filete', 'Filete de pescado', 4500.00, 4, 'Carnes', 'disponible', NULL, 'Proveedor Carnes'),
(66, 'Pan Integral', 'Pan integral', 800.00, 20, 'Panadería', 'disponible', NULL, 'Proveedor Panadería'),
(67, 'Croissants', 'Croissants', 600.00, 15, 'Panadería', 'disponible', NULL, 'Proveedor Panadería'),
(68, 'Tortillas', 'Tortillas de harina', 1000.00, 12, 'Panadería', 'disponible', NULL, 'Proveedor Panadería'),
(69, 'Baguette', 'Baguette francesa', 700.00, 10, 'Panadería', 'disponible', NULL, 'Proveedor Panadería'),
(70, 'Muffins', 'Muffins caseros', 800.00, 15, 'Panadería', 'disponible', NULL, 'Proveedor Panadería'),
(71, 'Donas', 'Donas glaseadas', 500.00, 20, 'Panadería', 'disponible', NULL, 'Proveedor Panadería'),
(72, 'Torta', 'Torta de chocolate', 2500.00, 3, 'Panadería', 'disponible', NULL, 'Proveedor Panadería'),
(73, 'Empanadas', 'Empanadas de pino', 800.00, 25, 'Panadería', 'disponible', NULL, 'Proveedor Panadería'),
(74, 'Jugo', 'Jugo de naranja', 1000.00, 20, 'Bebidas', 'disponible', NULL, 'Proveedor Central'),
(75, 'Agua', 'Agua mineral', 500.00, 50, 'Bebidas', 'disponible', NULL, 'Proveedor Central'),
(76, 'Refresco', 'Refresco cola', 800.00, 30, 'Bebidas', 'disponible', NULL, 'Proveedor Central'),
(77, 'Vino', 'Vino tinto', 2500.00, 15, 'Bebidas', 'disponible', NULL, 'Proveedor Central'),
(78, 'Cerveza', 'Cerveza nacional', 1200.00, 25, 'Bebidas', 'disponible', NULL, 'Proveedor Central'),
(79, 'Champagne', 'Champagne', 5000.00, 5, 'Bebidas', 'disponible', NULL, 'Proveedor Central'),
(80, 'Whisky', 'Whisky escocés', 8000.00, 3, 'Bebidas', 'disponible', NULL, 'Proveedor Central'),
(81, 'Ron', 'Ron añejo', 6000.00, 4, 'Bebidas', 'disponible', NULL, 'Proveedor Central'),
(82, 'Sal', 'Sal marina', 300.00, 20, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(83, 'Azúcar', 'Azúcar blanca', 1000.00, 15, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(84, 'Aceite', 'Aceite vegetal', 2500.00, 10, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(85, 'Pimienta', 'Pimienta negra', 1200.00, 12, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(86, 'Orégano', 'Orégano seco', 800.00, 15, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(87, 'Comino', 'Comino molido', 1000.00, 10, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(88, 'Ajo', 'Ajo fresco', 600.00, 20, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(89, 'Cebolla', 'Cebolla deshidratada', 900.00, 15, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(90, 'Laurel', 'Hojas de laurel', 500.00, 8, 'Condimentos', 'disponible', NULL, 'Proveedor Central'),
(91, 'Sardinas', 'Sardinas en lata', 1200.00, 12, 'Conservas', 'disponible', NULL, 'Proveedor Sur'),
(92, 'Champiñones', 'Champiñones en lata', 1600.00, 8, 'Conservas', 'disponible', NULL, 'Proveedor Sur'),
(93, 'Palmitos', 'Palmitos en conserva', 2500.00, 6, 'Conservas', 'disponible', NULL, 'Proveedor Sur'),
(94, 'Alcachofas', 'Alcachofas en conserva', 2000.00, 5, 'Conservas', 'disponible', NULL, 'Proveedor Sur'),
(95, 'Espárragos', 'Espárragos en conserva', 2200.00, 4, 'Conservas', 'disponible', NULL, 'Proveedor Sur'),
(96, 'Chocolate', 'Chocolate negro', 2000.00, 15, 'Dulces', 'disponible', NULL, 'Proveedor Central'),
(97, 'Caramelos', 'Caramelos surtidos', 800.00, 30, 'Dulces', 'disponible', NULL, 'Proveedor Central'),
(98, 'Chicles', 'Chicles de menta', 500.00, 40, 'Dulces', 'disponible', NULL, 'Proveedor Central'),
(99, 'Turrón', 'Turrón de almendras', 3000.00, 8, 'Dulces', 'disponible', NULL, 'Proveedor Central'),
(100, 'Mermelada', 'Mermelada de fresa', 1200.00, 12, 'Dulces', 'disponible', NULL, 'Proveedor Central'),
(101, 'Mantecol', 'Mantecol chileno', 1500.00, 15, 'Dulces', 'disponible', NULL, 'Proveedor Central'),
(102, 'Alfajores', 'Alfajores surtidos', 1000.00, 20, 'Dulces', 'disponible', NULL, 'Proveedor Central'),
(103, 'Oreos', 'Galletas Oreo', 1500.00, 18, 'Dulces', 'disponible', NULL, 'Proveedor Central'),
(104, 'Papas Fritas', 'Papas fritas', 1200.00, 25, 'Snacks', 'disponible', NULL, 'Proveedor Central'),
(105, 'Detergente', 'Detergente líquido', 2000.00, 15, 'Limpieza', 'disponible', NULL, 'Proveedor Central'),
(106, 'Jabón', 'Jabón de tocador', 800.00, 30, 'Limpieza', 'disponible', NULL, 'Proveedor Central'),
(107, 'Shampoo', 'Shampoo familiar', 2500.00, 12, 'Limpieza', 'disponible', NULL, 'Proveedor Central'),
(108, 'Papel', 'Papel higiénico', 1500.00, 20, 'Limpieza', 'disponible', NULL, 'Proveedor Central'),
(109, 'Toallas', 'Toallas de papel', 1000.00, 15, 'Limpieza', 'disponible', NULL, 'Proveedor Central'),
(110, 'Limpiavidrios', 'Limpiavidrios', 1200.00, 10, 'Limpieza', 'disponible', NULL, 'Proveedor Central'),
(111, 'Desinfectante', 'Desinfectante', 1800.00, 8, 'Limpieza', 'disponible', NULL, 'Proveedor Central'),
(112, 'Escoba', 'Escoba de paja', 2500.00, 5, 'Limpieza', 'disponible', NULL, 'Proveedor Central'),
(113, 'Trapo', 'Trapo de cocina', 500.00, 20, 'Limpieza', 'disponible', NULL, 'Proveedor Central'),
(114, 'Esponja', 'Esponja de cocina', 300.00, 25, 'Limpieza', 'disponible', NULL, 'Proveedor Central'),
(115, 'Cepillo', 'Cepillo de dientes', 800.00, 20, 'Higiene', 'disponible', NULL, 'Proveedor Central'),
(116, 'Pasta', 'Pasta dental', 1200.00, 15, 'Higiene', 'disponible', NULL, 'Proveedor Central'),
(117, 'Hilo', 'Hilo dental', 600.00, 25, 'Higiene', 'disponible', NULL, 'Proveedor Central'),
(118, 'Desodorante', 'Desodorante', 1500.00, 12, 'Higiene', 'disponible', NULL, 'Proveedor Central'),
(119, 'Protector', 'Protector solar', 3000.00, 8, 'Higiene', 'disponible', NULL, 'Proveedor Central'),
(120, 'Cotonitos', 'Cotonitos', 500.00, 30, 'Higiene', 'disponible', NULL, 'Proveedor Central'),
(121, 'Pañales', 'Pañales bebé', 4000.00, 10, 'Higiene', 'disponible', NULL, 'Proveedor Central'),
(122, 'Toallitas', 'Toallitas húmedas', 1800.00, 12, 'Higiene', 'disponible', NULL, 'Proveedor Central'),
(123, 'Laptop HP Pavilion', '', 450000.00, 10, 'Electrónicos', '', NULL, ''),
(124, 'Mouse Inalámbrico', '', 25000.00, 38, 'Accesorios', '', NULL, ''),
(125, 'Teclado Mecánico', '', 85000.00, 24, 'Accesorios', '', NULL, ''),
(126, 'Monitor 24\"', '', 180000.00, 12, 'Monitores', '', NULL, ''),
(127, 'Auriculares Bluetooth', '', 65000.00, 31, 'Audio', '', NULL, ''),
(128, 'Webcam HD', '', 45000.00, 18, 'Accesorios', '', NULL, ''),
(129, 'Tablet Samsung', '', 320000.00, 5, 'Electrónicos', '', NULL, ''),
(130, 'Cargador USB-C', '', 15000.00, 52, 'Accesorios', '', NULL, ''),
(131, 'Disco Duro 1TB', '', 120000.00, 13, 'Almacenamiento', '', NULL, ''),
(132, 'Memoria RAM 8GB', '', 75000.00, 25, 'Componentes', '', NULL, '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(6, 'auth_app', 'usuario'),
(4, 'contenttypes', 'contenttype'),
(10, 'djangoVerVictorMondaca', 'clientes'),
(11, 'djangoVerVictorMondaca', 'productos'),
(5, 'sessions', 'session'),
(12, 'ventas_app', 'controldia'),
(8, 'ventas_app', 'itemventa'),
(9, 'ventas_app', 'resumendiario'),
(7, 'ventas_app', 'venta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-10-08 00:26:53.363636'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-10-08 00:26:53.399642'),
(3, 'auth', '0001_initial', '2025-10-08 00:26:53.523050'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-10-08 00:26:53.544830'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-10-08 00:26:53.547159'),
(6, 'auth', '0004_alter_user_username_opts', '2025-10-08 00:26:53.550977'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-10-08 00:26:53.553250'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-10-08 00:26:53.553709'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-10-08 00:26:53.555491'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-10-08 00:26:53.557130'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-10-08 00:26:53.559239'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-10-08 00:26:53.570919'),
(13, 'auth', '0011_update_proxy_permissions', '2025-10-08 00:26:53.574433'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-10-08 00:26:53.576969'),
(15, 'auth_app', '0001_initial', '2025-10-08 00:26:53.710166'),
(16, 'admin', '0001_initial', '2025-10-08 00:26:53.780836'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-10-08 00:26:53.784519'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-10-08 00:26:53.788240'),
(19, 'djangoVerVictorMondaca', '0001_initial', '2025-10-08 00:26:53.797027'),
(20, 'djangoVerVictorMondaca', '0002_clientes_productos_delete_empleado', '2025-10-08 00:26:53.816040'),
(21, 'djangoVerVictorMondaca', '0003_auto_20251006_2223', '2025-10-08 00:26:53.816657'),
(22, 'djangoVerVictorMondaca', '0004_auto_20250107_2125', '2025-10-08 00:26:53.998948'),
(23, 'sessions', '0001_initial', '2025-10-08 00:26:54.027237'),
(24, 'djangoVerVictorMondaca', '0005_alter_clientes_options_and_more', '2025-10-08 00:27:02.730107'),
(25, 'ventas_app', '0001_initial', '2025-10-08 00:27:02.898476'),
(26, 'ventas_app', '0002_controldia', '2025-10-08 01:00:42.649383');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2lt4xzkz0t6s9ots46d2fkm2wgdpzeyp', 'e30:1v6I2w:9j_hh70b89j64xPEA9sN81Mea6RB2Z4s9U6AiST1mKY', '2025-10-22 00:28:46.441978'),
('3pindk8vb8ikeeifbjobt5nirl79mh0f', '.eJxVjDsOwjAQBe_iGlmJ48-Gkj5nsHbXaxxAjpRPhbg7iZQC2jcz760ibmuJ2yJzHJO6qlZdfjdCfko9QHpgvU-ap7rOI-lD0Sdd9DAled1O9--g4FL2Wsg2Yvomc0fGAhAxIdoehBMEQB84h93pAFwykh2RC5ycN-Jd06L6fAEG0TiX:1v6Icz:4JSv2T4FTZL1iFXmnwIgRGGypeI2AJWF_RZgBqzqdWk', '2025-10-22 01:06:01.281480'),
('pczoq9iy3dr9somc989ecz9emxx045u2', 'e30:1v6I2S:iQH1eRluoPD0K9BwvIVefT5z2LdawO6ydcwBTrZyl1w', '2025-10-22 00:28:16.064368');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_app_controldia`
--

CREATE TABLE `ventas_app_controldia` (
  `id` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `estado` varchar(20) NOT NULL,
  `fecha_apertura` datetime(6) NOT NULL,
  `fecha_cierre` datetime(6) DEFAULT NULL,
  `observaciones` longtext NOT NULL,
  `usuario_apertura_id` bigint(20) DEFAULT NULL,
  `usuario_cierre_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas_app_controldia`
--

INSERT INTO `ventas_app_controldia` (`id`, `fecha`, `estado`, `fecha_apertura`, `fecha_cierre`, `observaciones`, `usuario_apertura_id`, `usuario_cierre_id`) VALUES
(1, '2025-10-07', 'abierto', '2025-10-08 01:13:54.236537', NULL, '', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_app_itemventa`
--

CREATE TABLE `ventas_app_itemventa` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(10) UNSIGNED NOT NULL CHECK (`cantidad` >= 0),
  `precio_unitario` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `producto_id` bigint(20) NOT NULL,
  `venta_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas_app_itemventa`
--

INSERT INTO `ventas_app_itemventa` (`id`, `cantidad`, `precio_unitario`, `subtotal`, `producto_id`, `venta_id`) VALUES
(2, 1, 600.00, 600.00, 4, 7),
(3, 2, 700.00, 1400.00, 7, 7),
(4, 2, 700.00, 1400.00, 7, 8),
(5, 1, 1000.00, 1000.00, 3, 9),
(6, 1, 700.00, 700.00, 7, 9),
(7, 2, 800.00, 1600.00, 2, 10),
(8, 2, 1200.00, 2400.00, 1, 10),
(9, 2, 800.00, 1600.00, 8, 11),
(10, 1, 1000.00, 1000.00, 10, 11),
(11, 2, 1200.00, 2400.00, 116, 12),
(12, 2, 3500.00, 7000.00, 60, 12),
(13, 3, 1500.00, 4500.00, 108, 12),
(14, 3, 1500.00, 4500.00, 45, 12),
(15, 1, 1400.00, 1400.00, 51, 12),
(16, 3, 1800.00, 5400.00, 122, 13),
(17, 1, 3000.00, 3000.00, 32, 13),
(18, 3, 800.00, 2400.00, 70, 13),
(19, 2, 800.00, 1600.00, 106, 13),
(20, 2, 1600.00, 3200.00, 92, 13),
(21, 3, 800.00, 2400.00, 115, 14),
(22, 1, 1200.00, 1200.00, 52, 14),
(23, 1, 500.00, 500.00, 75, 15),
(24, 2, 6000.00, 12000.00, 81, 15),
(25, 2, 800.00, 1600.00, 20, 15),
(26, 1, 800.00, 800.00, 106, 15),
(27, 1, 1000.00, 1000.00, 102, 16),
(28, 3, 2500.00, 7500.00, 61, 17),
(29, 1, 8000.00, 8000.00, 80, 18),
(30, 1, 2000.00, 2000.00, 22, 18),
(31, 3, 300.00, 900.00, 18, 18),
(32, 2, 800.00, 1600.00, 106, 18),
(33, 1, 1800.00, 1800.00, 23, 18),
(34, 2, 2000.00, 4000.00, 105, 19),
(35, 3, 2500.00, 7500.00, 37, 19),
(36, 3, 1000.00, 3000.00, 17, 19),
(37, 3, 2500.00, 7500.00, 31, 19),
(38, 1, 1200.00, 1200.00, 11, 19),
(39, 1, 1200.00, 1200.00, 1, 20),
(40, 2, 800.00, 1600.00, 8, 21),
(41, 2, 700.00, 1400.00, 69, 21),
(42, 3, 1000.00, 3000.00, 74, 21),
(43, 1, 1200.00, 1200.00, 100, 22),
(44, 3, 1000.00, 3000.00, 3, 22),
(45, 3, 1600.00, 4800.00, 92, 22),
(46, 3, 2200.00, 6600.00, 63, 23),
(47, 1, 2500.00, 2500.00, 84, 23),
(48, 3, 4000.00, 12000.00, 44, 24),
(49, 1, 600.00, 600.00, 67, 24),
(50, 2, 2000.00, 4000.00, 25, 25),
(51, 3, 500.00, 1500.00, 75, 25),
(52, 2, 2000.00, 4000.00, 105, 25),
(53, 2, 2500.00, 5000.00, 93, 25),
(54, 3, 2000.00, 6000.00, 22, 25),
(55, 3, 1800.00, 5400.00, 23, 26),
(56, 1, 2500.00, 2500.00, 107, 27),
(57, 3, 800.00, 2400.00, 86, 27),
(58, 2, 1000.00, 2000.00, 74, 27),
(59, 3, 2000.00, 6000.00, 96, 27),
(60, 1, 2500.00, 2500.00, 112, 27),
(61, 2, 1500.00, 3000.00, 118, 28),
(62, 3, 900.00, 2700.00, 6, 28),
(63, 1, 1600.00, 1600.00, 36, 29),
(64, 1, 1600.00, 1600.00, 92, 29),
(65, 3, 2500.00, 7500.00, 77, 29),
(66, 1, 800.00, 800.00, 33, 29),
(67, 1, 1000.00, 1000.00, 49, 29),
(68, 3, 3000.00, 9000.00, 26, 30),
(69, 3, 600.00, 1800.00, 88, 30),
(70, 2, 2500.00, 5000.00, 31, 30),
(71, 3, 1800.00, 5400.00, 122, 30),
(72, 3, 3000.00, 9000.00, 38, 30),
(73, 2, 500.00, 1000.00, 71, 31),
(74, 2, 1500.00, 3000.00, 24, 31),
(75, 1, 2000.00, 2000.00, 105, 31),
(76, 1, 1500.00, 1500.00, 57, 31),
(77, 3, 1200.00, 3600.00, 28, 31),
(78, 3, 600.00, 1800.00, 14, 32),
(79, 1, 1500.00, 1500.00, 41, 32),
(80, 2, 1200.00, 2400.00, 91, 32),
(81, 2, 2500.00, 5000.00, 19, 32),
(82, 3, 1200.00, 3600.00, 85, 32),
(83, 1, 2000.00, 2000.00, 96, 33),
(84, 3, 2000.00, 6000.00, 34, 33),
(85, 2, 1200.00, 2400.00, 104, 33),
(86, 2, 4000.00, 8000.00, 121, 33),
(87, 2, 800.00, 1600.00, 86, 34),
(88, 2, 600.00, 1200.00, 4, 34),
(89, 1, 2000.00, 2000.00, 46, 34),
(90, 3, 800.00, 2400.00, 66, 34),
(91, 1, 1200.00, 1200.00, 85, 35),
(92, 3, 1500.00, 4500.00, 30, 36),
(93, 3, 5000.00, 15000.00, 79, 36),
(94, 1, 1200.00, 1200.00, 85, 36),
(95, 2, 500.00, 1000.00, 120, 36),
(96, 2, 1600.00, 3200.00, 92, 37),
(97, 3, 1000.00, 3000.00, 10, 37),
(98, 2, 800.00, 1600.00, 33, 37),
(99, 2, 2200.00, 4400.00, 48, 37),
(100, 2, 2500.00, 5000.00, 27, 37),
(101, 1, 2000.00, 2000.00, 25, 38),
(102, 2, 1800.00, 3600.00, 122, 39),
(103, 2, 5000.00, 10000.00, 79, 39),
(104, 2, 3000.00, 6000.00, 26, 39),
(105, 2, 1400.00, 2800.00, 51, 39),
(106, 3, 2000.00, 6000.00, 96, 40),
(107, 1, 2200.00, 2200.00, 95, 40),
(108, 2, 1600.00, 3200.00, 92, 40),
(109, 2, 1800.00, 3600.00, 23, 40),
(110, 3, 3000.00, 9000.00, 58, 40),
(111, 3, 1200.00, 3600.00, 116, 41),
(112, 3, 1500.00, 4500.00, 5, 42),
(113, 3, 2500.00, 7500.00, 31, 42),
(114, 1, 2500.00, 2500.00, 112, 42),
(115, 1, 3000.00, 3000.00, 99, 42),
(116, 2, 800.00, 1600.00, 13, 42),
(117, 2, 1200.00, 2400.00, 85, 43),
(118, 2, 500.00, 1000.00, 71, 44),
(119, 3, 2000.00, 6000.00, 25, 44),
(120, 2, 1500.00, 3000.00, 103, 45),
(121, 2, 600.00, 1200.00, 14, 45),
(122, 3, 800.00, 2400.00, 20, 46),
(123, 1, 2800.00, 2800.00, 64, 46),
(124, 1, 500.00, 500.00, 75, 46),
(125, 1, 1200.00, 1200.00, 1, 46),
(126, 2, 1500.00, 3000.00, 101, 47),
(127, 2, 5000.00, 10000.00, 79, 47),
(128, 3, 1200.00, 3600.00, 52, 47),
(129, 2, 500.00, 1000.00, 120, 47),
(130, 3, 1500.00, 4500.00, 45, 48),
(131, 1, 1200.00, 1200.00, 9, 49),
(132, 3, 1200.00, 3600.00, 116, 49),
(133, 2, 800.00, 1600.00, 73, 49),
(134, 1, 1800.00, 1800.00, 35, 49),
(135, 2, 3000.00, 6000.00, 55, 50),
(136, 2, 1600.00, 3200.00, 50, 50),
(137, 1, 1500.00, 1500.00, 5, 50),
(138, 2, 2000.00, 4000.00, 25, 50),
(139, 1, 1800.00, 1800.00, 23, 51),
(140, 3, 800.00, 2400.00, 70, 52),
(141, 3, 1200.00, 3600.00, 9, 52),
(142, 1, 2000.00, 2000.00, 22, 52),
(143, 1, 500.00, 500.00, 71, 52),
(144, 2, 4500.00, 9000.00, 65, 52),
(145, 1, 1000.00, 1000.00, 17, 53),
(146, 3, 700.00, 2100.00, 7, 54),
(147, 1, 1200.00, 1200.00, 9, 54),
(148, 3, 500.00, 1500.00, 113, 54),
(149, 1, 1000.00, 1000.00, 49, 54),
(150, 1, 2500.00, 2500.00, 19, 55),
(151, 3, 900.00, 2700.00, 89, 55),
(152, 1, 500.00, 500.00, 90, 56),
(153, 2, 1800.00, 3600.00, 53, 56),
(154, 1, 2500.00, 2500.00, 19, 56),
(155, 3, 4000.00, 12000.00, 59, 56),
(156, 2, 1000.00, 2000.00, 68, 56),
(157, 1, 1500.00, 1500.00, 57, 57),
(158, 2, 8000.00, 16000.00, 80, 57),
(159, 3, 1200.00, 3600.00, 28, 58),
(160, 2, 5000.00, 10000.00, 79, 58),
(161, 2, 2500.00, 5000.00, 61, 58),
(162, 2, 1200.00, 2400.00, 21, 58),
(163, 3, 800.00, 2400.00, 76, 59),
(164, 2, 2800.00, 5600.00, 64, 59),
(165, 1, 2200.00, 2200.00, 48, 59),
(166, 2, 800.00, 1600.00, 70, 59),
(167, 1, 4000.00, 4000.00, 59, 60),
(168, 3, 2500.00, 7500.00, 72, 60),
(169, 3, 2800.00, 8400.00, 64, 60),
(170, 3, 1000.00, 3000.00, 74, 60),
(171, 1, 1000.00, 1000.00, 74, 61),
(172, 3, 800.00, 2400.00, 70, 61),
(173, 1, 3000.00, 3000.00, 26, 61),
(174, 1, 300.00, 300.00, 18, 61),
(175, 3, 2000.00, 6000.00, 42, 61),
(176, 2, 800.00, 1600.00, 16, 62),
(177, 2, 1000.00, 2000.00, 3, 62),
(178, 1, 2500.00, 2500.00, 112, 62),
(179, 2, 1200.00, 2400.00, 39, 62),
(180, 3, 1800.00, 5400.00, 23, 63),
(181, 1, 2200.00, 2200.00, 95, 63),
(182, 1, 1200.00, 1200.00, 9, 63),
(183, 2, 1800.00, 3600.00, 122, 63),
(184, 3, 3500.00, 10500.00, 60, 64),
(185, 3, 800.00, 2400.00, 13, 64),
(186, 1, 800.00, 800.00, 73, 65),
(187, 3, 1600.00, 4800.00, 50, 66),
(188, 2, 8000.00, 16000.00, 80, 67),
(189, 2, 2500.00, 5000.00, 61, 68),
(190, 2, 1600.00, 3200.00, 92, 68),
(191, 2, 1800.00, 3600.00, 23, 69),
(192, 1, 1000.00, 1000.00, 40, 69),
(193, 3, 500.00, 1500.00, 98, 69),
(194, 3, 900.00, 2700.00, 6, 69),
(195, 2, 1200.00, 2400.00, 21, 69),
(196, 2, 500.00, 1000.00, 98, 70),
(197, 3, 800.00, 2400.00, 76, 70),
(198, 2, 800.00, 1600.00, 106, 70),
(199, 2, 1000.00, 2000.00, 83, 71),
(200, 1, 500.00, 500.00, 90, 71),
(201, 1, 800.00, 800.00, 106, 72),
(202, 2, 800.00, 1600.00, 13, 72),
(203, 2, 1500.00, 3000.00, 41, 73),
(204, 3, 600.00, 1800.00, 117, 74),
(205, 2, 2000.00, 4000.00, 22, 74),
(206, 3, 2000.00, 6000.00, 94, 74),
(207, 3, 2500.00, 7500.00, 72, 74),
(208, 2, 2000.00, 4000.00, 25, 75),
(209, 3, 3000.00, 9000.00, 38, 75),
(210, 1, 900.00, 900.00, 6, 75),
(211, 2, 2200.00, 4400.00, 63, 75),
(212, 1, 1000.00, 1000.00, 49, 75),
(213, 3, 1000.00, 3000.00, 49, 76),
(214, 3, 3500.00, 10500.00, 60, 76),
(215, 1, 1800.00, 1800.00, 122, 76),
(216, 3, 1200.00, 3600.00, 116, 76),
(217, 3, 1500.00, 4500.00, 41, 76),
(218, 3, 1200.00, 3600.00, 15, 77),
(219, 1, 1800.00, 1800.00, 53, 78),
(220, 2, 500.00, 1000.00, 75, 78),
(221, 3, 4000.00, 12000.00, 44, 78),
(222, 2, 1400.00, 2800.00, 51, 78),
(223, 2, 600.00, 1200.00, 14, 78),
(224, 2, 1800.00, 3600.00, 43, 79),
(225, 1, 800.00, 800.00, 8, 79),
(226, 2, 1200.00, 2400.00, 85, 79),
(227, 2, 3000.00, 6000.00, 58, 80),
(228, 2, 1800.00, 3600.00, 43, 80),
(229, 3, 1200.00, 3600.00, 78, 80),
(230, 1, 800.00, 800.00, 76, 80),
(231, 1, 2500.00, 2500.00, 107, 81),
(232, 3, 800.00, 2400.00, 16, 81),
(233, 2, 4000.00, 8000.00, 121, 81),
(234, 3, 2000.00, 6000.00, 34, 82),
(235, 3, 1000.00, 3000.00, 102, 82),
(236, 2, 3000.00, 6000.00, 99, 82),
(237, 3, 500.00, 1500.00, 75, 83),
(238, 1, 1500.00, 1500.00, 41, 84),
(239, 2, 800.00, 1600.00, 13, 84),
(240, 3, 700.00, 2100.00, 7, 84),
(241, 2, 600.00, 1200.00, 14, 85),
(242, 1, 600.00, 600.00, 4, 85),
(243, 2, 4000.00, 8000.00, 59, 86),
(244, 1, 2500.00, 2500.00, 27, 87),
(245, 3, 1800.00, 5400.00, 47, 87),
(246, 3, 500.00, 1500.00, 120, 87),
(247, 3, 2800.00, 8400.00, 64, 87),
(248, 2, 800.00, 1600.00, 70, 87),
(249, 3, 2500.00, 7500.00, 84, 88),
(250, 1, 500.00, 500.00, 71, 88),
(251, 2, 500.00, 1000.00, 98, 88),
(252, 2, 800.00, 1600.00, 2, 88),
(253, 3, 2000.00, 6000.00, 62, 89),
(254, 1, 800.00, 800.00, 70, 89),
(255, 1, 1600.00, 1600.00, 92, 90),
(256, 3, 1500.00, 4500.00, 101, 90),
(257, 2, 2000.00, 4000.00, 34, 90),
(258, 2, 2500.00, 5000.00, 93, 90),
(259, 2, 1000.00, 2000.00, 102, 91),
(260, 1, 1500.00, 1500.00, 24, 91),
(261, 1, 700.00, 700.00, 7, 92),
(262, 1, 1200.00, 1200.00, 9, 93),
(263, 1, 800.00, 800.00, 97, 93),
(264, 3, 300.00, 900.00, 114, 93),
(265, 2, 1200.00, 2400.00, 15, 94),
(266, 3, 1000.00, 3000.00, 3, 94),
(267, 3, 4000.00, 12000.00, 59, 95),
(268, 1, 1800.00, 1800.00, 53, 95),
(269, 2, 3000.00, 6000.00, 32, 96),
(270, 2, 1200.00, 2400.00, 1, 96),
(271, 1, 1200.00, 1200.00, 91, 97),
(272, 2, 1800.00, 3600.00, 111, 97),
(273, 3, 900.00, 2700.00, 6, 97),
(274, 1, 800.00, 800.00, 16, 98),
(275, 3, 2000.00, 6000.00, 105, 98),
(276, 2, 8000.00, 16000.00, 80, 98),
(277, 3, 2000.00, 6000.00, 94, 98),
(278, 1, 800.00, 800.00, 20, 98),
(279, 3, 1500.00, 4500.00, 57, 99),
(280, 1, 2500.00, 2500.00, 37, 99),
(281, 1, 1000.00, 1000.00, 87, 99),
(282, 1, 3000.00, 3000.00, 38, 99),
(283, 3, 2500.00, 7500.00, 77, 100),
(284, 2, 1800.00, 3600.00, 23, 100),
(285, 2, 2500.00, 5000.00, 31, 100),
(286, 1, 1500.00, 1500.00, 108, 100),
(287, 1, 2200.00, 2200.00, 48, 100),
(288, 3, 1200.00, 3600.00, 100, 101),
(289, 2, 2500.00, 5000.00, 31, 101),
(290, 1, 2000.00, 2000.00, 25, 101),
(291, 2, 600.00, 1200.00, 67, 102),
(292, 3, 1600.00, 4800.00, 36, 102),
(293, 2, 1200.00, 2400.00, 78, 102),
(294, 1, 1500.00, 1500.00, 45, 103),
(295, 1, 800.00, 800.00, 29, 103),
(296, 3, 3000.00, 9000.00, 58, 103),
(297, 3, 600.00, 1800.00, 88, 104),
(298, 1, 4500.00, 4500.00, 65, 105),
(299, 2, 2500.00, 5000.00, 31, 105),
(300, 1, 500.00, 500.00, 120, 105),
(301, 1, 3000.00, 3000.00, 38, 106),
(302, 3, 800.00, 2400.00, 86, 106),
(303, 3, 2800.00, 8400.00, 64, 106),
(304, 1, 2500.00, 2500.00, 77, 106),
(305, 2, 2500.00, 5000.00, 19, 106),
(306, 1, 800.00, 800.00, 16, 107),
(307, 3, 2500.00, 7500.00, 107, 107),
(308, 1, 2000.00, 2000.00, 46, 107),
(309, 2, 1500.00, 3000.00, 5, 107),
(310, 1, 1800.00, 1800.00, 47, 107),
(311, 2, 1500.00, 3000.00, 108, 108),
(312, 3, 800.00, 2400.00, 20, 108),
(313, 3, 2500.00, 7500.00, 31, 108),
(314, 3, 1500.00, 4500.00, 57, 108),
(315, 2, 3000.00, 6000.00, 55, 109),
(316, 2, 1500.00, 3000.00, 118, 109),
(317, 1, 1000.00, 1000.00, 102, 110),
(318, 1, 500.00, 500.00, 120, 111),
(319, 1, 2500.00, 2500.00, 112, 111),
(320, 2, 900.00, 1800.00, 89, 112),
(321, 3, 600.00, 1800.00, 4, 113),
(322, 1, 2000.00, 2000.00, 22, 114),
(323, 3, 500.00, 1500.00, 120, 114),
(324, 1, 700.00, 700.00, 7, 114),
(325, 2, 1800.00, 3600.00, 47, 114),
(326, 3, 1500.00, 4500.00, 5, 115),
(327, 3, 2800.00, 8400.00, 64, 116),
(328, 3, 1200.00, 3600.00, 52, 117),
(329, 2, 1500.00, 3000.00, 45, 117),
(330, 3, 1500.00, 4500.00, 24, 118),
(331, 3, 500.00, 1500.00, 75, 118),
(332, 2, 1500.00, 3000.00, 101, 118),
(333, 1, 1800.00, 1800.00, 122, 118),
(334, 1, 800.00, 800.00, 16, 119),
(335, 1, 800.00, 800.00, 76, 119),
(336, 3, 800.00, 2400.00, 70, 119),
(337, 3, 1000.00, 3000.00, 83, 120),
(338, 3, 2500.00, 7500.00, 27, 121),
(339, 2, 2000.00, 4000.00, 105, 121),
(340, 3, 1000.00, 3000.00, 87, 121),
(341, 2, 1500.00, 3000.00, 30, 121),
(342, 3, 800.00, 2400.00, 97, 122),
(343, 3, 1600.00, 4800.00, 50, 122),
(344, 1, 300.00, 300.00, 82, 122),
(345, 1, 2000.00, 2000.00, 105, 123),
(346, 2, 1500.00, 3000.00, 101, 123),
(347, 1, 600.00, 600.00, 67, 123),
(348, 2, 1000.00, 2000.00, 68, 123),
(349, 3, 1200.00, 3600.00, 104, 123),
(350, 3, 900.00, 2700.00, 6, 124),
(351, 1, 2000.00, 2000.00, 46, 124),
(352, 1, 1200.00, 1200.00, 104, 124),
(353, 2, 800.00, 1600.00, 115, 125),
(354, 2, 1000.00, 2000.00, 102, 126),
(355, 1, 2500.00, 2500.00, 37, 126),
(356, 1, 6000.00, 6000.00, 81, 126),
(357, 2, 2500.00, 5000.00, 84, 127),
(358, 1, 2200.00, 2200.00, 95, 127),
(359, 3, 2800.00, 8400.00, 64, 128),
(360, 2, 900.00, 1800.00, 89, 129),
(361, 2, 800.00, 1600.00, 73, 129),
(362, 2, 1800.00, 3600.00, 122, 130),
(363, 3, 600.00, 1800.00, 14, 130),
(364, 1, 1000.00, 1000.00, 102, 130),
(365, 1, 1000.00, 1000.00, 68, 131),
(366, 3, 4500.00, 13500.00, 65, 131),
(367, 2, 3000.00, 6000.00, 99, 132),
(368, 1, 300.00, 300.00, 18, 132),
(369, 3, 800.00, 2400.00, 115, 132),
(370, 3, 1200.00, 3600.00, 116, 133),
(371, 1, 2200.00, 2200.00, 95, 133),
(372, 1, 1500.00, 1500.00, 57, 133),
(373, 2, 300.00, 600.00, 114, 134),
(374, 3, 5000.00, 15000.00, 79, 134),
(375, 3, 500.00, 1500.00, 75, 134),
(376, 1, 500.00, 500.00, 98, 134),
(377, 3, 800.00, 2400.00, 20, 135),
(378, 1, 500.00, 500.00, 98, 135),
(379, 3, 500.00, 1500.00, 90, 135),
(380, 3, 1000.00, 3000.00, 10, 135),
(381, 2, 900.00, 1800.00, 89, 136),
(382, 2, 1000.00, 2000.00, 109, 136),
(383, 3, 2500.00, 7500.00, 77, 137),
(384, 1, 1200.00, 1200.00, 78, 137),
(385, 1, 2500.00, 2500.00, 93, 137),
(386, 1, 1800.00, 1800.00, 23, 137),
(387, 3, 1500.00, 4500.00, 101, 137),
(388, 2, 3000.00, 6000.00, 38, 138),
(389, 1, 1500.00, 1500.00, 45, 138),
(390, 3, 1200.00, 3600.00, 39, 138),
(391, 3, 2000.00, 6000.00, 94, 138),
(392, 1, 1500.00, 1500.00, 30, 139),
(393, 2, 800.00, 1600.00, 2, 139),
(394, 2, 300.00, 600.00, 82, 140),
(395, 1, 800.00, 800.00, 97, 140),
(396, 1, 900.00, 900.00, 6, 140),
(397, 3, 4000.00, 12000.00, 121, 140),
(398, 1, 2000.00, 2000.00, 62, 141),
(399, 3, 8000.00, 24000.00, 80, 141),
(400, 2, 600.00, 1200.00, 88, 141),
(401, 2, 1500.00, 3000.00, 45, 141),
(402, 1, 2500.00, 2500.00, 27, 142),
(403, 3, 1200.00, 3600.00, 1, 143),
(404, 2, 1000.00, 2000.00, 40, 143),
(405, 1, 2000.00, 2000.00, 46, 143),
(406, 3, 2500.00, 7500.00, 84, 143),
(407, 1, 1400.00, 1400.00, 51, 143),
(408, 2, 2500.00, 5000.00, 27, 144),
(409, 3, 1800.00, 5400.00, 23, 144),
(410, 1, 1200.00, 1200.00, 110, 144),
(411, 1, 800.00, 800.00, 115, 145),
(412, 2, 1200.00, 2400.00, 15, 145),
(413, 2, 2500.00, 5000.00, 77, 145),
(414, 1, 2800.00, 2800.00, 64, 146),
(415, 1, 4000.00, 4000.00, 121, 146),
(416, 3, 600.00, 1800.00, 117, 146),
(417, 1, 1200.00, 1200.00, 28, 146),
(418, 3, 1000.00, 3000.00, 83, 146),
(419, 2, 1000.00, 2000.00, 10, 147),
(420, 1, 1000.00, 1000.00, 17, 147),
(421, 3, 5000.00, 15000.00, 79, 148),
(422, 2, 1800.00, 3600.00, 111, 148),
(423, 1, 2500.00, 2500.00, 27, 148),
(424, 3, 1000.00, 3000.00, 109, 148),
(425, 3, 1800.00, 5400.00, 47, 149),
(426, 1, 1600.00, 1600.00, 56, 149),
(427, 1, 3000.00, 3000.00, 32, 149),
(428, 2, 2000.00, 4000.00, 42, 150),
(429, 1, 1000.00, 1000.00, 49, 150),
(430, 1, 2200.00, 2200.00, 95, 150),
(431, 3, 2500.00, 7500.00, 61, 150),
(432, 3, 2500.00, 7500.00, 31, 150),
(433, 1, 800.00, 800.00, 20, 151),
(434, 3, 500.00, 1500.00, 120, 151),
(435, 1, 1500.00, 1500.00, 57, 152),
(436, 1, 2500.00, 2500.00, 107, 152),
(437, 1, 1200.00, 1200.00, 116, 152),
(438, 2, 1000.00, 2000.00, 3, 153),
(439, 3, 1600.00, 4800.00, 56, 153),
(440, 1, 800.00, 800.00, 16, 153),
(441, 2, 2000.00, 4000.00, 62, 154),
(442, 3, 2200.00, 6600.00, 63, 154),
(443, 3, 1000.00, 3000.00, 10, 154),
(444, 2, 900.00, 1800.00, 6, 154),
(445, 1, 3000.00, 3000.00, 119, 154),
(446, 3, 1200.00, 3600.00, 116, 155),
(447, 2, 2000.00, 4000.00, 25, 155),
(448, 3, 3000.00, 9000.00, 58, 155),
(449, 1, 3000.00, 3000.00, 32, 155),
(450, 2, 4000.00, 8000.00, 44, 156),
(451, 1, 2500.00, 2500.00, 77, 156),
(452, 1, 300.00, 300.00, 82, 156),
(453, 1, 1500.00, 1500.00, 41, 156),
(454, 3, 3500.00, 10500.00, 60, 156),
(455, 3, 1000.00, 3000.00, 10, 157),
(456, 1, 800.00, 800.00, 29, 157),
(457, 1, 8000.00, 8000.00, 80, 157),
(458, 2, 4500.00, 9000.00, 65, 158),
(459, 2, 1000.00, 2000.00, 3, 158),
(460, 1, 2500.00, 2500.00, 84, 158),
(461, 2, 2500.00, 5000.00, 19, 158),
(462, 1, 2000.00, 2000.00, 25, 158),
(463, 3, 1800.00, 5400.00, 47, 159),
(464, 2, 4500.00, 9000.00, 65, 159),
(465, 2, 900.00, 1800.00, 89, 159),
(466, 1, 8000.00, 8000.00, 80, 160),
(467, 1, 3000.00, 3000.00, 32, 160),
(468, 3, 1800.00, 5400.00, 53, 160),
(469, 2, 2200.00, 4400.00, 48, 160),
(470, 2, 2000.00, 4000.00, 46, 161),
(471, 2, 1800.00, 3600.00, 122, 162),
(472, 2, 1800.00, 3600.00, 111, 162),
(473, 3, 1200.00, 3600.00, 116, 162),
(474, 3, 2800.00, 8400.00, 64, 162),
(475, 1, 4000.00, 4000.00, 121, 162),
(476, 2, 800.00, 1600.00, 20, 163),
(477, 3, 1500.00, 4500.00, 24, 164),
(478, 1, 1000.00, 1000.00, 49, 164),
(479, 2, 1800.00, 3600.00, 23, 164),
(480, 1, 1500.00, 1500.00, 57, 165),
(481, 2, 300.00, 600.00, 114, 165),
(482, 2, 600.00, 1200.00, 88, 165),
(483, 1, 2500.00, 2500.00, 72, 166),
(484, 3, 1000.00, 3000.00, 109, 166),
(485, 2, 2500.00, 5000.00, 27, 166),
(486, 3, 900.00, 2700.00, 6, 166),
(487, 1, 600.00, 600.00, 67, 167),
(488, 3, 4000.00, 12000.00, 121, 167),
(489, 2, 1800.00, 3600.00, 23, 167),
(490, 2, 800.00, 1600.00, 106, 168),
(491, 3, 2500.00, 7500.00, 31, 168),
(492, 2, 1200.00, 2400.00, 15, 168),
(493, 1, 3000.00, 3000.00, 26, 168),
(494, 2, 1800.00, 3600.00, 23, 169),
(495, 1, 1000.00, 1000.00, 10, 169),
(496, 1, 2500.00, 2500.00, 27, 170),
(497, 1, 600.00, 600.00, 14, 170),
(498, 3, 1500.00, 4500.00, 24, 170),
(499, 1, 1200.00, 1200.00, 1, 170),
(500, 2, 500.00, 1000.00, 90, 170),
(501, 3, 800.00, 2400.00, 73, 171),
(502, 1, 1800.00, 1800.00, 35, 171),
(503, 2, 3000.00, 6000.00, 119, 171),
(504, 3, 500.00, 1500.00, 120, 172),
(505, 2, 800.00, 1600.00, 106, 172),
(506, 1, 1600.00, 1600.00, 56, 172),
(507, 2, 800.00, 1600.00, 115, 173),
(508, 3, 1200.00, 3600.00, 100, 173),
(509, 1, 1500.00, 1500.00, 12, 173),
(510, 1, 1000.00, 1000.00, 74, 173),
(511, 1, 3000.00, 3000.00, 32, 173),
(512, 2, 1000.00, 2000.00, 83, 174),
(513, 1, 3000.00, 3000.00, 26, 174),
(514, 3, 2500.00, 7500.00, 31, 174),
(515, 2, 2500.00, 5000.00, 107, 174),
(516, 3, 800.00, 2400.00, 70, 174),
(517, 2, 2200.00, 4400.00, 63, 175),
(518, 2, 1500.00, 3000.00, 24, 175),
(519, 2, 1600.00, 3200.00, 56, 175),
(520, 2, 3500.00, 7000.00, 60, 175),
(521, 3, 2000.00, 6000.00, 46, 176),
(522, 2, 800.00, 1600.00, 29, 177),
(523, 1, 1200.00, 1200.00, 91, 178),
(524, 3, 1200.00, 3600.00, 116, 179),
(525, 3, 2500.00, 7500.00, 93, 180),
(526, 1, 900.00, 900.00, 6, 181),
(527, 2, 2000.00, 4000.00, 42, 181),
(528, 3, 1500.00, 4500.00, 118, 181),
(529, 1, 2200.00, 2200.00, 63, 181),
(530, 1, 2500.00, 2500.00, 54, 182),
(531, 3, 8000.00, 24000.00, 80, 182),
(532, 2, 1200.00, 2400.00, 1, 182),
(533, 2, 1800.00, 3600.00, 23, 182),
(534, 1, 500.00, 500.00, 120, 183),
(535, 1, 500.00, 500.00, 75, 183),
(536, 2, 300.00, 600.00, 114, 183),
(537, 1, 800.00, 800.00, 13, 183),
(538, 1, 800.00, 800.00, 16, 183),
(539, 1, 1500.00, 1500.00, 12, 184),
(540, 2, 1500.00, 3000.00, 5, 184),
(541, 2, 2800.00, 5600.00, 64, 184),
(542, 2, 1500.00, 3000.00, 45, 184),
(543, 1, 1500.00, 1500.00, 30, 185),
(544, 3, 1600.00, 4800.00, 36, 185),
(545, 3, 800.00, 2400.00, 76, 185),
(546, 2, 2500.00, 5000.00, 112, 185),
(547, 3, 1200.00, 3600.00, 78, 185),
(548, 1, 3000.00, 3000.00, 55, 186),
(549, 2, 4000.00, 8000.00, 59, 186),
(550, 2, 1500.00, 3000.00, 45, 186),
(551, 3, 1200.00, 3600.00, 104, 186),
(552, 2, 600.00, 1200.00, 14, 187),
(553, 3, 800.00, 2400.00, 66, 187),
(554, 2, 2200.00, 4400.00, 63, 188),
(555, 2, 1000.00, 2000.00, 40, 188),
(556, 1, 800.00, 800.00, 73, 189),
(557, 3, 1200.00, 3600.00, 28, 189),
(558, 2, 1600.00, 3200.00, 36, 190),
(559, 3, 1600.00, 4800.00, 56, 190),
(560, 3, 1000.00, 3000.00, 3, 190),
(561, 3, 500.00, 1500.00, 98, 190),
(562, 1, 2500.00, 2500.00, 107, 191),
(563, 3, 500.00, 1500.00, 71, 191),
(564, 3, 1200.00, 3600.00, 15, 191),
(565, 2, 1500.00, 3000.00, 12, 191),
(566, 3, 1600.00, 4800.00, 36, 191),
(567, 1, 1800.00, 1800.00, 111, 192),
(568, 1, 8000.00, 8000.00, 80, 192),
(569, 2, 800.00, 1600.00, 106, 192),
(570, 1, 500.00, 500.00, 75, 193),
(571, 3, 3000.00, 9000.00, 32, 193),
(572, 1, 800.00, 800.00, 16, 194),
(573, 2, 1000.00, 2000.00, 17, 194),
(574, 3, 1200.00, 3600.00, 1, 194),
(575, 2, 800.00, 1600.00, 76, 194),
(576, 2, 1200.00, 2400.00, 11, 195),
(577, 2, 800.00, 1600.00, 2, 195),
(578, 3, 2200.00, 6600.00, 48, 196),
(579, 1, 1800.00, 1800.00, 43, 196),
(580, 1, 2000.00, 2000.00, 105, 196),
(581, 1, 500.00, 500.00, 71, 197),
(582, 3, 500.00, 1500.00, 113, 197),
(583, 2, 1800.00, 3600.00, 47, 197),
(584, 2, 1000.00, 2000.00, 87, 198),
(585, 2, 600.00, 1200.00, 67, 198),
(586, 1, 2500.00, 2500.00, 84, 198),
(587, 1, 5000.00, 5000.00, 79, 198),
(588, 2, 2000.00, 4000.00, 42, 199),
(589, 1, 1400.00, 1400.00, 51, 200),
(590, 2, 1200.00, 2400.00, 9, 200),
(591, 3, 800.00, 2400.00, 97, 201),
(592, 2, 4000.00, 8000.00, 44, 202),
(593, 2, 1800.00, 3600.00, 47, 202),
(594, 1, 1000.00, 1000.00, 3, 202),
(595, 3, 2200.00, 6600.00, 48, 202),
(596, 1, 500.00, 500.00, 75, 202),
(597, 3, 8000.00, 24000.00, 80, 203),
(598, 1, 800.00, 800.00, 16, 203),
(599, 1, 1600.00, 1600.00, 92, 203),
(600, 3, 5000.00, 15000.00, 79, 203),
(601, 2, 300.00, 600.00, 82, 204),
(602, 2, 1000.00, 2000.00, 68, 204),
(603, 1, 800.00, 800.00, 2, 204),
(604, 3, 800.00, 2400.00, 86, 204),
(605, 2, 800.00, 1600.00, 76, 204),
(606, 2, 1500.00, 3000.00, 57, 205),
(607, 2, 600.00, 1200.00, 117, 205),
(608, 3, 1000.00, 3000.00, 87, 205),
(609, 3, 1600.00, 4800.00, 56, 206),
(610, 1, 1200.00, 1200.00, 1, 206),
(611, 1, 1200.00, 1200.00, 78, 207),
(612, 1, 1800.00, 1800.00, 53, 208),
(613, 1, 2800.00, 2800.00, 64, 208),
(614, 2, 1600.00, 3200.00, 92, 208),
(615, 2, 600.00, 1200.00, 4, 208),
(616, 3, 2200.00, 6600.00, 95, 209),
(617, 1, 1000.00, 1000.00, 87, 209),
(618, 1, 800.00, 800.00, 2, 209),
(619, 3, 900.00, 2700.00, 6, 209),
(620, 1, 300.00, 300.00, 114, 209),
(621, 3, 2200.00, 6600.00, 48, 210),
(622, 3, 1200.00, 3600.00, 15, 210),
(623, 1, 800.00, 800.00, 8, 210),
(624, 2, 1200.00, 2400.00, 116, 210),
(625, 2, 300.00, 600.00, 114, 210),
(626, 1, 1200.00, 1200.00, 15, 211),
(627, 3, 1500.00, 4500.00, 57, 211),
(628, 3, 1600.00, 4800.00, 92, 211),
(629, 3, 1000.00, 3000.00, 102, 211),
(630, 1, 1500.00, 1500.00, 12, 211),
(631, 3, 2500.00, 7500.00, 31, 212),
(632, 3, 1800.00, 5400.00, 47, 213),
(633, 1, 1000.00, 1000.00, 49, 214),
(634, 2, 300.00, 600.00, 18, 214),
(635, 2, 5000.00, 10000.00, 79, 214),
(636, 2, 3000.00, 6000.00, 38, 215),
(637, 2, 8000.00, 16000.00, 80, 215),
(638, 1, 1500.00, 1500.00, 45, 216),
(639, 2, 4000.00, 8000.00, 121, 216),
(640, 1, 2500.00, 2500.00, 72, 217),
(641, 3, 500.00, 1500.00, 71, 217),
(642, 3, 1200.00, 3600.00, 52, 218),
(643, 1, 1000.00, 1000.00, 17, 219),
(644, 2, 800.00, 1600.00, 8, 219),
(645, 3, 900.00, 2700.00, 6, 219),
(646, 3, 800.00, 2400.00, 33, 219),
(647, 3, 600.00, 1800.00, 117, 220),
(648, 2, 800.00, 1600.00, 76, 220),
(649, 1, 4000.00, 4000.00, 59, 220),
(650, 1, 2500.00, 2500.00, 72, 220),
(651, 2, 3000.00, 6000.00, 58, 221),
(652, 1, 600.00, 600.00, 88, 221),
(653, 2, 2000.00, 4000.00, 94, 221),
(654, 2, 300.00, 600.00, 82, 221),
(655, 3, 1200.00, 3600.00, 11, 222),
(656, 2, 300.00, 600.00, 82, 222),
(657, 2, 1000.00, 2000.00, 10, 223),
(658, 2, 500.00, 1000.00, 75, 223),
(659, 3, 1000.00, 3000.00, 17, 224),
(660, 2, 1500.00, 3000.00, 30, 224),
(661, 1, 2800.00, 2800.00, 64, 224),
(662, 1, 4000.00, 4000.00, 121, 224),
(663, 2, 5000.00, 10000.00, 79, 225),
(664, 1, 2200.00, 2200.00, 63, 225),
(665, 1, 2500.00, 2500.00, 54, 225),
(666, 1, 2500.00, 2500.00, 61, 226),
(667, 1, 1600.00, 1600.00, 36, 226),
(668, 1, 1000.00, 1000.00, 10, 227),
(669, 2, 1500.00, 3000.00, 24, 228),
(670, 2, 4500.00, 9000.00, 65, 228),
(671, 1, 1200.00, 1200.00, 116, 228),
(672, 2, 2200.00, 4400.00, 95, 229),
(673, 1, 1800.00, 1800.00, 53, 230),
(674, 2, 4000.00, 8000.00, 44, 230),
(675, 2, 500.00, 1000.00, 71, 230),
(676, 1, 1200.00, 1200.00, 15, 231),
(677, 1, 500.00, 500.00, 90, 231),
(678, 2, 1000.00, 2000.00, 74, 231),
(679, 1, 1200.00, 1200.00, 9, 232),
(680, 1, 600.00, 600.00, 88, 233),
(681, 2, 2500.00, 5000.00, 27, 234),
(682, 2, 1200.00, 2400.00, 110, 234),
(683, 1, 600.00, 600.00, 14, 234),
(684, 1, 800.00, 800.00, 106, 235),
(685, 2, 1400.00, 2800.00, 51, 235),
(686, 1, 800.00, 800.00, 2, 236),
(687, 1, 300.00, 300.00, 82, 236),
(688, 1, 1200.00, 1200.00, 100, 237),
(689, 1, 800.00, 800.00, 66, 237),
(690, 1, 800.00, 800.00, 33, 238),
(691, 1, 2000.00, 2000.00, 105, 238),
(692, 2, 1800.00, 3600.00, 47, 238),
(693, 1, 800.00, 800.00, 106, 239),
(694, 2, 800.00, 1600.00, 29, 240),
(695, 1, 2000.00, 2000.00, 25, 241),
(696, 1, 1500.00, 1500.00, 5, 241),
(697, 2, 500.00, 1000.00, 75, 241),
(698, 1, 800.00, 800.00, 2, 242),
(699, 2, 500.00, 1000.00, 90, 243),
(700, 2, 3000.00, 6000.00, 38, 244),
(701, 2, 1000.00, 2000.00, 83, 244),
(702, 1, 1200.00, 1200.00, 1, 245),
(703, 2, 800.00, 1600.00, 33, 246),
(704, 1, 1500.00, 1500.00, 103, 246),
(705, 2, 800.00, 1600.00, 20, 247),
(706, 1, 1500.00, 1500.00, 45, 247),
(707, 2, 800.00, 1600.00, 97, 248),
(708, 2, 500.00, 1000.00, 113, 248),
(709, 1, 600.00, 600.00, 4, 249),
(710, 2, 1500.00, 3000.00, 5, 250),
(711, 2, 1000.00, 2000.00, 49, 250),
(712, 1, 1500.00, 1500.00, 118, 250),
(713, 1, 1500.00, 1500.00, 24, 251),
(714, 2, 1000.00, 2000.00, 83, 252),
(715, 2, 2000.00, 4000.00, 22, 252),
(716, 1, 1500.00, 1500.00, 41, 253),
(717, 2, 2000.00, 4000.00, 46, 254),
(718, 2, 2500.00, 5000.00, 19, 255),
(719, 2, 1000.00, 2000.00, 40, 255),
(720, 2, 1000.00, 2000.00, 87, 256),
(721, 2, 4000.00, 8000.00, 121, 257),
(722, 1, 1200.00, 1200.00, 1, 257),
(723, 1, 300.00, 300.00, 18, 258),
(724, 1, 1200.00, 1200.00, 100, 259),
(725, 1, 1000.00, 1000.00, 40, 259),
(726, 2, 4000.00, 8000.00, 44, 259),
(727, 2, 1000.00, 2000.00, 40, 260),
(728, 2, 800.00, 1600.00, 97, 260),
(729, 2, 4000.00, 8000.00, 59, 260),
(730, 1, 1200.00, 1200.00, 1, 261),
(735, 2, 85000.00, 170000.00, 125, 263),
(736, 3, 15000.00, 45000.00, 130, 263),
(737, 2, 65000.00, 130000.00, 127, 264),
(738, 3, 450000.00, 1350000.00, 123, 264),
(739, 1, 75000.00, 75000.00, 132, 264),
(740, 3, 15000.00, 45000.00, 130, 264),
(741, 2, 120000.00, 240000.00, 131, 265),
(742, 3, 25000.00, 75000.00, 124, 266),
(743, 1, 45000.00, 45000.00, 128, 266),
(744, 3, 180000.00, 540000.00, 126, 266),
(745, 1, 320000.00, 320000.00, 129, 267),
(746, 2, 25000.00, 50000.00, 124, 267),
(747, 1, 75000.00, 75000.00, 132, 267),
(748, 1, 65000.00, 65000.00, 127, 268),
(749, 2, 120000.00, 240000.00, 131, 268),
(750, 1, 75000.00, 75000.00, 132, 268),
(751, 2, 450000.00, 900000.00, 123, 268),
(752, 1, 75000.00, 75000.00, 132, 269),
(753, 2, 15000.00, 30000.00, 130, 269),
(754, 3, 320000.00, 960000.00, 129, 269),
(755, 2, 65000.00, 130000.00, 127, 270),
(756, 3, 45000.00, 135000.00, 128, 270),
(757, 1, 320000.00, 320000.00, 129, 270),
(758, 3, 25000.00, 75000.00, 124, 270),
(759, 1, 65000.00, 65000.00, 127, 271),
(760, 3, 75000.00, 225000.00, 132, 271),
(761, 2, 25000.00, 50000.00, 124, 271),
(762, 2, 180000.00, 360000.00, 126, 271),
(763, 2, 85000.00, 170000.00, 125, 272),
(764, 1, 320000.00, 320000.00, 129, 273),
(765, 3, 45000.00, 135000.00, 128, 274),
(766, 2, 25000.00, 50000.00, 124, 274),
(767, 2, 65000.00, 130000.00, 127, 274),
(768, 2, 75000.00, 150000.00, 132, 274),
(769, 2, 180000.00, 360000.00, 126, 275),
(770, 1, 65000.00, 65000.00, 127, 276),
(771, 1, 120000.00, 120000.00, 131, 276),
(772, 1, 180000.00, 180000.00, 126, 276),
(773, 1, 320000.00, 320000.00, 129, 277),
(774, 2, 85000.00, 170000.00, 125, 277),
(775, 1, 75000.00, 75000.00, 132, 277),
(776, 35, 1500.00, 52500.00, 5, 278);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_app_resumendiario`
--

CREATE TABLE `ventas_app_resumendiario` (
  `id` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `total_ventas` int(11) NOT NULL,
  `total_boletas` int(11) NOT NULL,
  `total_facturas` int(11) NOT NULL,
  `subtotal_dia` decimal(12,2) NOT NULL,
  `iva_dia` decimal(12,2) NOT NULL,
  `total_dia` decimal(12,2) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas_app_resumendiario`
--

INSERT INTO `ventas_app_resumendiario` (`id`, `fecha`, `total_ventas`, `total_boletas`, `total_facturas`, `subtotal_dia`, `iva_dia`, `total_dia`, `fecha_creacion`) VALUES
(1, '2025-10-08', 0, 0, 0, 0.00, 0.00, 0.00, '2025-10-08 00:37:19.987306');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_app_venta`
--

CREATE TABLE `ventas_app_venta` (
  `id` bigint(20) NOT NULL,
  `numero_venta` varchar(20) NOT NULL,
  `fecha_venta` datetime(6) NOT NULL,
  `tipo_documento` varchar(10) NOT NULL,
  `estado` varchar(10) NOT NULL,
  `rut_cliente` varchar(12) DEFAULT NULL,
  `direccion_cliente` varchar(200) DEFAULT NULL,
  `comuna_cliente` varchar(50) DEFAULT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `iva` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `forma_pago` varchar(20) NOT NULL,
  `observaciones` longtext DEFAULT NULL,
  `cliente_id` int(11) DEFAULT NULL,
  `vendedor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas_app_venta`
--

INSERT INTO `ventas_app_venta` (`id`, `numero_venta`, `fecha_venta`, `tipo_documento`, `estado`, `rut_cliente`, `direccion_cliente`, `comuna_cliente`, `subtotal`, `iva`, `total`, `forma_pago`, `observaciones`, `cliente_id`, `vendedor_id`) VALUES
(7, 'V202510070007', '2025-10-08 01:15:09.712381', 'factura', 'completada', NULL, NULL, NULL, 2000.00, 380.00, 2380.00, 'transferencia', NULL, 239, 1),
(8, 'V202510070008', '2025-10-08 01:15:09.724372', 'boleta', 'completada', NULL, NULL, NULL, 1400.00, 266.00, 1666.00, 'efectivo', NULL, 296, 4),
(9, 'V202510070009', '2025-10-08 01:15:09.729025', 'factura', 'completada', NULL, NULL, NULL, 1700.00, 323.00, 2023.00, 'efectivo', NULL, 107, 4),
(10, 'V202510070010', '2025-10-08 01:15:09.735400', 'boleta', 'completada', NULL, NULL, NULL, 4000.00, 760.00, 4760.00, 'efectivo', NULL, 107, 1),
(11, 'V202510070011', '2025-10-08 01:15:09.739280', 'factura', 'completada', NULL, NULL, NULL, 2600.00, 494.00, 3094.00, 'efectivo', NULL, 224, 4),
(12, 'V202508220012', '2025-10-08 01:19:12.213436', 'boleta', 'completada', NULL, NULL, NULL, 19800.00, 3762.00, 23562.00, 'efectivo', NULL, 116, 8),
(13, 'V202505250013', '2025-10-08 01:19:12.241143', 'boleta', 'completada', NULL, NULL, NULL, 15600.00, 2964.00, 18564.00, 'tarjeta_debito', NULL, 16, 11),
(14, 'V202506230014', '2025-10-08 01:19:12.254864', 'boleta', 'completada', NULL, NULL, NULL, 3600.00, 684.00, 4284.00, 'tarjeta_credito', NULL, 325, 7),
(15, 'V202507260015', '2025-10-08 01:19:12.258967', 'factura', 'completada', NULL, NULL, NULL, 14900.00, 2831.00, 17731.00, 'efectivo', NULL, 504, 10),
(16, 'V202509080016', '2025-10-08 01:19:12.265247', 'boleta', 'completada', NULL, NULL, NULL, 1000.00, 190.00, 1190.00, 'tarjeta_debito', NULL, 154, 9),
(17, 'V202507080017', '2025-10-08 01:19:12.267468', 'factura', 'completada', NULL, NULL, NULL, 7500.00, 1425.00, 8925.00, 'transferencia', NULL, 13, 12),
(18, 'V202508230018', '2025-10-08 01:19:12.280810', 'boleta', 'completada', NULL, NULL, NULL, 14300.00, 2717.00, 17017.00, 'transferencia', NULL, 215, 11),
(19, 'V202505190019', '2025-10-08 01:19:12.294741', 'boleta', 'completada', NULL, NULL, NULL, 23200.00, 4408.00, 27608.00, 'tarjeta_credito', NULL, 427, 11),
(20, 'V202509270020', '2025-10-08 01:19:12.300368', 'boleta', 'completada', NULL, NULL, NULL, 1200.00, 228.00, 1428.00, 'efectivo', NULL, 504, 6),
(21, 'V202505010021', '2025-10-08 01:19:12.303969', 'boleta', 'completada', NULL, NULL, NULL, 6000.00, 1140.00, 7140.00, 'transferencia', NULL, 190, 5),
(22, 'V202509260022', '2025-10-08 01:19:12.313427', 'factura', 'completada', NULL, NULL, NULL, 9000.00, 1710.00, 10710.00, 'tarjeta_credito', NULL, 240, 6),
(23, 'V202508310023', '2025-10-08 01:19:12.325374', 'factura', 'completada', NULL, NULL, NULL, 9100.00, 1729.00, 10829.00, 'transferencia', NULL, 49, 7),
(24, 'V202509200024', '2025-10-08 01:19:12.333314', 'factura', 'completada', NULL, NULL, NULL, 12600.00, 2394.00, 14994.00, 'tarjeta_debito', NULL, 120, 1),
(25, 'V202506140025', '2025-10-08 01:19:12.338600', 'boleta', 'completada', NULL, NULL, NULL, 20500.00, 3895.00, 24395.00, 'transferencia', NULL, 313, 4),
(26, 'V202505090026', '2025-10-08 01:19:12.346228', 'boleta', 'completada', NULL, NULL, NULL, 5400.00, 1026.00, 6426.00, 'transferencia', NULL, 361, 8),
(27, 'V202505230027', '2025-10-08 01:19:12.348943', 'factura', 'completada', NULL, NULL, NULL, 15400.00, 2926.00, 18326.00, 'tarjeta_debito', NULL, 127, 5),
(28, 'V202508180028', '2025-10-08 01:19:12.354149', 'factura', 'completada', NULL, NULL, NULL, 5700.00, 1083.00, 6783.00, 'efectivo', NULL, 199, 11),
(29, 'V202505070029', '2025-10-08 01:19:12.357502', 'boleta', 'completada', NULL, NULL, NULL, 12500.00, 2375.00, 14875.00, 'tarjeta_debito', NULL, 324, 9),
(30, 'V202505210030', '2025-10-08 01:19:12.362953', 'boleta', 'completada', NULL, NULL, NULL, 30200.00, 5738.00, 35938.00, 'transferencia', NULL, 88, 5),
(31, 'V202509100031', '2025-10-08 01:19:12.366684', 'boleta', 'completada', NULL, NULL, NULL, 11100.00, 2109.00, 13209.00, 'tarjeta_debito', NULL, 228, 11),
(32, 'V202505030032', '2025-10-08 01:19:12.371010', 'factura', 'completada', NULL, NULL, NULL, 14300.00, 2717.00, 17017.00, 'transferencia', NULL, 52, 4),
(33, 'V202507220033', '2025-10-08 01:19:12.377319', 'boleta', 'completada', NULL, NULL, NULL, 18400.00, 3496.00, 21896.00, 'transferencia', NULL, 99, 5),
(34, 'V202506120034', '2025-10-08 01:19:12.384198', 'factura', 'completada', NULL, NULL, NULL, 7200.00, 1368.00, 8568.00, 'tarjeta_credito', NULL, 381, 6),
(35, 'V202509270035', '2025-10-08 01:19:12.389135', 'factura', 'completada', NULL, NULL, NULL, 1200.00, 228.00, 1428.00, 'tarjeta_credito', NULL, 3, 7),
(36, 'V202508010036', '2025-10-08 01:19:12.393635', 'factura', 'completada', NULL, NULL, NULL, 21700.00, 4123.00, 25823.00, 'efectivo', NULL, 197, 10),
(37, 'V202506080037', '2025-10-08 01:19:12.399334', 'boleta', 'completada', NULL, NULL, NULL, 17200.00, 3268.00, 20468.00, 'efectivo', NULL, 436, 1),
(38, 'V202508270038', '2025-10-08 01:19:12.404090', 'factura', 'completada', NULL, NULL, NULL, 2000.00, 380.00, 2380.00, 'tarjeta_credito', NULL, 246, 8),
(39, 'V202509120039', '2025-10-08 01:19:12.407572', 'boleta', 'completada', NULL, NULL, NULL, 22400.00, 4256.00, 26656.00, 'transferencia', NULL, 441, 1),
(40, 'V202507120040', '2025-10-08 01:19:12.416078', 'boleta', 'completada', NULL, NULL, NULL, 24000.00, 4560.00, 28560.00, 'efectivo', NULL, 180, 5),
(41, 'V202507030041', '2025-10-08 01:19:12.422064', 'boleta', 'completada', NULL, NULL, NULL, 3600.00, 684.00, 4284.00, 'tarjeta_debito', NULL, 92, 1),
(42, 'V202504130042', '2025-10-08 01:19:12.424669', 'boleta', 'completada', NULL, NULL, NULL, 19100.00, 3629.00, 22729.00, 'efectivo', NULL, 75, 9),
(43, 'V202508160043', '2025-10-08 01:19:12.430270', 'boleta', 'completada', NULL, NULL, NULL, 2400.00, 456.00, 2856.00, 'transferencia', NULL, 414, 6),
(44, 'V202504110044', '2025-10-08 01:19:12.432587', 'factura', 'completada', NULL, NULL, NULL, 7000.00, 1330.00, 8330.00, 'transferencia', NULL, 345, 10),
(45, 'V202505130045', '2025-10-08 01:19:12.434991', 'factura', 'completada', NULL, NULL, NULL, 4200.00, 798.00, 4998.00, 'tarjeta_debito', NULL, 447, 4),
(46, 'V202510030046', '2025-10-08 01:19:12.438228', 'boleta', 'completada', NULL, NULL, NULL, 6900.00, 1311.00, 8211.00, 'transferencia', NULL, 43, 10),
(47, 'V202504260047', '2025-10-08 01:19:12.441927', 'boleta', 'completada', NULL, NULL, NULL, 17600.00, 3344.00, 20944.00, 'tarjeta_debito', NULL, 46, 1),
(48, 'V202506210048', '2025-10-08 01:19:12.447840', 'boleta', 'completada', NULL, NULL, NULL, 4500.00, 855.00, 5355.00, 'transferencia', NULL, 351, 12),
(49, 'V202506010049', '2025-10-08 01:19:12.450260', 'factura', 'completada', NULL, NULL, NULL, 8200.00, 1558.00, 9758.00, 'transferencia', NULL, 498, 5),
(50, 'V202504180050', '2025-10-08 01:19:12.454135', 'factura', 'completada', NULL, NULL, NULL, 14700.00, 2793.00, 17493.00, 'tarjeta_debito', NULL, 385, 6),
(51, 'V202509300051', '2025-10-08 01:19:12.457990', 'factura', 'completada', NULL, NULL, NULL, 1800.00, 342.00, 2142.00, 'tarjeta_credito', NULL, 114, 10),
(52, 'V202509050052', '2025-10-08 01:19:12.461460', 'boleta', 'completada', NULL, NULL, NULL, 17500.00, 3325.00, 20825.00, 'tarjeta_credito', NULL, 322, 8),
(53, 'V202506160053', '2025-10-08 01:19:12.465799', 'factura', 'completada', NULL, NULL, NULL, 1000.00, 190.00, 1190.00, 'tarjeta_debito', NULL, 285, 10),
(54, 'V202509020054', '2025-10-08 01:19:12.468271', 'factura', 'completada', NULL, NULL, NULL, 5800.00, 1102.00, 6902.00, 'tarjeta_debito', NULL, 18, 8),
(55, 'V202507060055', '2025-10-08 01:19:12.476180', 'boleta', 'completada', NULL, NULL, NULL, 5200.00, 988.00, 6188.00, 'efectivo', NULL, 431, 7),
(56, 'V202508240056', '2025-10-08 01:19:12.482793', 'factura', 'completada', NULL, NULL, NULL, 20600.00, 3914.00, 24514.00, 'tarjeta_credito', NULL, 416, 6),
(57, 'V202507140057', '2025-10-08 01:19:12.491270', 'factura', 'completada', NULL, NULL, NULL, 17500.00, 3325.00, 20825.00, 'tarjeta_credito', NULL, 398, 8),
(58, 'V202506220058', '2025-10-08 01:19:12.495968', 'factura', 'completada', NULL, NULL, NULL, 21000.00, 3990.00, 24990.00, 'tarjeta_debito', NULL, 154, 10),
(59, 'V202505310059', '2025-10-08 01:19:12.515429', 'boleta', 'completada', NULL, NULL, NULL, 11800.00, 2242.00, 14042.00, 'transferencia', NULL, 322, 7),
(60, 'V202507090060', '2025-10-08 01:19:12.530199', 'boleta', 'completada', NULL, NULL, NULL, 22900.00, 4351.00, 27251.00, 'tarjeta_credito', NULL, 293, 4),
(61, 'V202505200061', '2025-10-08 01:19:12.540913', 'boleta', 'completada', NULL, NULL, NULL, 12700.00, 2413.00, 15113.00, 'efectivo', NULL, 279, 11),
(62, 'V202506300062', '2025-10-08 01:19:12.549925', 'boleta', 'completada', NULL, NULL, NULL, 8500.00, 1615.00, 10115.00, 'tarjeta_debito', NULL, 113, 1),
(63, 'V202507140063', '2025-10-08 01:19:12.562788', 'boleta', 'completada', NULL, NULL, NULL, 12400.00, 2356.00, 14756.00, 'efectivo', NULL, 189, 4),
(64, 'V202510050064', '2025-10-08 01:19:12.579422', 'boleta', 'completada', NULL, NULL, NULL, 12900.00, 2451.00, 15351.00, 'tarjeta_credito', NULL, 166, 12),
(65, 'V202505170065', '2025-10-08 01:19:12.590659', 'factura', 'completada', NULL, NULL, NULL, 800.00, 152.00, 952.00, 'tarjeta_credito', NULL, 27, 11),
(66, 'V202510020066', '2025-10-08 01:19:12.602653', 'factura', 'completada', NULL, NULL, NULL, 4800.00, 912.00, 5712.00, 'tarjeta_credito', NULL, 452, 1),
(67, 'V202509210067', '2025-10-08 01:19:12.608915', 'boleta', 'completada', NULL, NULL, NULL, 16000.00, 3040.00, 19040.00, 'tarjeta_debito', NULL, 423, 7),
(68, 'V202506200068', '2025-10-08 01:19:12.615774', 'boleta', 'completada', NULL, NULL, NULL, 8200.00, 1558.00, 9758.00, 'tarjeta_debito', NULL, 497, 5),
(69, 'V202507110069', '2025-10-08 01:19:12.621692', 'factura', 'completada', NULL, NULL, NULL, 11200.00, 2128.00, 13328.00, 'tarjeta_debito', NULL, 401, 7),
(70, 'V202506240070', '2025-10-08 01:19:12.630662', 'boleta', 'completada', NULL, NULL, NULL, 5000.00, 950.00, 5950.00, 'transferencia', NULL, 109, 8),
(71, 'V202507280071', '2025-10-08 01:19:12.635343', 'factura', 'completada', NULL, NULL, NULL, 2500.00, 475.00, 2975.00, 'tarjeta_debito', NULL, 371, 10),
(72, 'V202506150072', '2025-10-08 01:19:12.640221', 'factura', 'completada', NULL, NULL, NULL, 2400.00, 456.00, 2856.00, 'efectivo', NULL, 309, 12),
(73, 'V202507030073', '2025-10-08 01:19:12.645785', 'boleta', 'completada', NULL, NULL, NULL, 3000.00, 570.00, 3570.00, 'efectivo', NULL, 313, 7),
(74, 'V202508110074', '2025-10-08 01:19:12.650144', 'boleta', 'completada', NULL, NULL, NULL, 19300.00, 3667.00, 22967.00, 'transferencia', NULL, 93, 6),
(75, 'V202507090075', '2025-10-08 01:19:12.655525', 'boleta', 'completada', NULL, NULL, NULL, 19300.00, 3667.00, 22967.00, 'transferencia', NULL, 411, 7),
(76, 'V202507280076', '2025-10-08 01:19:12.671545', 'factura', 'completada', NULL, NULL, NULL, 23400.00, 4446.00, 27846.00, 'tarjeta_debito', NULL, 100, 10),
(77, 'V202507270077', '2025-10-08 01:19:12.683820', 'factura', 'completada', NULL, NULL, NULL, 3600.00, 684.00, 4284.00, 'efectivo', NULL, 33, 4),
(78, 'V202507130078', '2025-10-08 01:19:12.688435', 'boleta', 'completada', NULL, NULL, NULL, 18800.00, 3572.00, 22372.00, 'tarjeta_debito', NULL, 198, 9),
(79, 'V202507240079', '2025-10-08 01:19:12.703615', 'boleta', 'completada', NULL, NULL, NULL, 6800.00, 1292.00, 8092.00, 'tarjeta_credito', NULL, 352, 12),
(80, 'V202508130080', '2025-10-08 01:19:12.713856', 'factura', 'completada', NULL, NULL, NULL, 14000.00, 2660.00, 16660.00, 'efectivo', NULL, 90, 8),
(81, 'V202505170081', '2025-10-08 01:19:12.723573', 'factura', 'completada', NULL, NULL, NULL, 12900.00, 2451.00, 15351.00, 'efectivo', NULL, 32, 10),
(82, 'V202506030082', '2025-10-08 01:19:12.734817', 'boleta', 'completada', NULL, NULL, NULL, 15000.00, 2850.00, 17850.00, 'tarjeta_debito', NULL, 169, 8),
(83, 'V202509050083', '2025-10-08 01:19:12.748226', 'boleta', 'completada', NULL, NULL, NULL, 1500.00, 285.00, 1785.00, 'tarjeta_debito', NULL, 298, 9),
(84, 'V202507190084', '2025-10-08 01:19:12.763360', 'factura', 'completada', NULL, NULL, NULL, 5200.00, 988.00, 6188.00, 'tarjeta_credito', NULL, 362, 11),
(85, 'V202509300085', '2025-10-08 01:19:12.812145', 'boleta', 'completada', NULL, NULL, NULL, 1800.00, 342.00, 2142.00, 'transferencia', NULL, 331, 12),
(86, 'V202507130086', '2025-10-08 01:19:12.830530', 'factura', 'completada', NULL, NULL, NULL, 8000.00, 1520.00, 9520.00, 'tarjeta_credito', NULL, 460, 12),
(87, 'V202506200087', '2025-10-08 01:19:12.846837', 'factura', 'completada', NULL, NULL, NULL, 19400.00, 3686.00, 23086.00, 'tarjeta_credito', NULL, 451, 8),
(88, 'V202506250088', '2025-10-08 01:19:12.870828', 'boleta', 'completada', NULL, NULL, NULL, 10600.00, 2014.00, 12614.00, 'transferencia', NULL, 151, 4),
(89, 'V202509240089', '2025-10-08 01:19:12.880907', 'factura', 'completada', NULL, NULL, NULL, 6800.00, 1292.00, 8092.00, 'tarjeta_debito', NULL, 425, 7),
(90, 'V202510040090', '2025-10-08 01:19:12.896885', 'factura', 'completada', NULL, NULL, NULL, 15100.00, 2869.00, 17969.00, 'tarjeta_credito', NULL, 433, 11),
(91, 'V202504130091', '2025-10-08 01:19:12.918744', 'boleta', 'completada', NULL, NULL, NULL, 3500.00, 665.00, 4165.00, 'efectivo', NULL, 78, 11),
(92, 'V202508070092', '2025-10-08 01:19:12.935095', 'factura', 'completada', NULL, NULL, NULL, 700.00, 133.00, 833.00, 'tarjeta_debito', NULL, 484, 10),
(93, 'V202507030093', '2025-10-08 01:19:12.949522', 'factura', 'completada', NULL, NULL, NULL, 2900.00, 551.00, 3451.00, 'tarjeta_credito', NULL, 21, 8),
(94, 'V202506240094', '2025-10-08 01:19:12.976606', 'boleta', 'completada', NULL, NULL, NULL, 5400.00, 1026.00, 6426.00, 'efectivo', NULL, 59, 9),
(95, 'V202505010095', '2025-10-08 01:19:13.037051', 'factura', 'completada', NULL, NULL, NULL, 13800.00, 2622.00, 16422.00, 'transferencia', NULL, 140, 6),
(96, 'V202505110096', '2025-10-08 01:19:13.073853', 'boleta', 'completada', NULL, NULL, NULL, 8400.00, 1596.00, 9996.00, 'tarjeta_credito', NULL, 152, 11),
(97, 'V202508010097', '2025-10-08 01:19:13.092281', 'boleta', 'completada', NULL, NULL, NULL, 7500.00, 1425.00, 8925.00, 'transferencia', NULL, 28, 9),
(98, 'V202507270098', '2025-10-08 01:19:13.132183', 'boleta', 'completada', NULL, NULL, NULL, 29600.00, 5624.00, 35224.00, 'transferencia', NULL, 491, 5),
(99, 'V202505100099', '2025-10-08 01:19:13.154989', 'boleta', 'completada', NULL, NULL, NULL, 11000.00, 2090.00, 13090.00, 'tarjeta_debito', NULL, 12, 7),
(100, 'V202507010100', '2025-10-08 01:19:13.164461', 'boleta', 'completada', NULL, NULL, NULL, 19800.00, 3762.00, 23562.00, 'tarjeta_debito', NULL, 224, 6),
(101, 'V202506220101', '2025-10-08 01:19:13.191642', 'boleta', 'completada', NULL, NULL, NULL, 10600.00, 2014.00, 12614.00, 'tarjeta_credito', NULL, 327, 11),
(102, 'V202507170102', '2025-10-08 01:19:13.219913', 'boleta', 'completada', NULL, NULL, NULL, 8400.00, 1596.00, 9996.00, 'transferencia', NULL, 55, 7),
(103, 'V202506250103', '2025-10-08 01:19:13.257496', 'factura', 'completada', NULL, NULL, NULL, 11300.00, 2147.00, 13447.00, 'transferencia', NULL, 75, 4),
(104, 'V202506070104', '2025-10-08 01:19:13.282777', 'boleta', 'completada', NULL, NULL, NULL, 1800.00, 342.00, 2142.00, 'transferencia', NULL, 459, 10),
(105, 'V202504110105', '2025-10-08 01:19:13.323525', 'factura', 'completada', NULL, NULL, NULL, 10000.00, 1900.00, 11900.00, 'tarjeta_debito', NULL, 136, 12),
(106, 'V202507230106', '2025-10-08 01:19:13.344453', 'factura', 'completada', NULL, NULL, NULL, 21300.00, 4047.00, 25347.00, 'transferencia', NULL, 147, 8),
(107, 'V202506180107', '2025-10-08 01:19:13.377004', 'boleta', 'completada', NULL, NULL, NULL, 15100.00, 2869.00, 17969.00, 'transferencia', NULL, 235, 9),
(108, 'V202504120108', '2025-10-08 01:19:13.423527', 'factura', 'completada', NULL, NULL, NULL, 17400.00, 3306.00, 20706.00, 'tarjeta_debito', NULL, 253, 1),
(109, 'V202509020109', '2025-10-08 01:19:13.451953', 'boleta', 'completada', NULL, NULL, NULL, 9000.00, 1710.00, 10710.00, 'tarjeta_credito', NULL, 466, 10),
(110, 'V202508310110', '2025-10-08 01:19:13.473865', 'factura', 'completada', NULL, NULL, NULL, 1000.00, 190.00, 1190.00, 'tarjeta_credito', NULL, 32, 8),
(111, 'V202508070111', '2025-10-08 01:19:13.488835', 'factura', 'completada', NULL, NULL, NULL, 3000.00, 570.00, 3570.00, 'tarjeta_debito', NULL, 234, 9),
(112, 'V202508250112', '2025-10-08 01:19:13.509407', 'factura', 'completada', NULL, NULL, NULL, 1800.00, 342.00, 2142.00, 'efectivo', NULL, 146, 1),
(113, 'V202509180113', '2025-10-08 01:19:13.531615', 'factura', 'completada', NULL, NULL, NULL, 1800.00, 342.00, 2142.00, 'tarjeta_credito', NULL, 187, 7),
(114, 'V202509230114', '2025-10-08 01:19:13.554777', 'boleta', 'completada', NULL, NULL, NULL, 7800.00, 1482.00, 9282.00, 'tarjeta_credito', NULL, 484, 6),
(115, 'V202508200115', '2025-10-08 01:19:13.643045', 'factura', 'completada', NULL, NULL, NULL, 4500.00, 855.00, 5355.00, 'transferencia', NULL, 501, 10),
(116, 'V202507180116', '2025-10-08 01:19:13.658227', 'factura', 'completada', NULL, NULL, NULL, 8400.00, 1596.00, 9996.00, 'tarjeta_debito', NULL, 305, 12),
(117, 'V202507040117', '2025-10-08 01:19:13.670277', 'boleta', 'completada', NULL, NULL, NULL, 6600.00, 1254.00, 7854.00, 'tarjeta_credito', NULL, 511, 8),
(118, 'V202507090118', '2025-10-08 01:19:13.682733', 'factura', 'completada', NULL, NULL, NULL, 10800.00, 2052.00, 12852.00, 'tarjeta_credito', NULL, 470, 5),
(119, 'V202506090119', '2025-10-08 01:19:13.710023', 'boleta', 'completada', NULL, NULL, NULL, 4000.00, 760.00, 4760.00, 'transferencia', NULL, 125, 7),
(120, 'V202505030120', '2025-10-08 01:19:13.752656', 'boleta', 'completada', NULL, NULL, NULL, 3000.00, 570.00, 3570.00, 'tarjeta_credito', NULL, 420, 11),
(121, 'V202509110121', '2025-10-08 01:19:13.774985', 'boleta', 'completada', NULL, NULL, NULL, 17500.00, 3325.00, 20825.00, 'efectivo', NULL, 174, 10),
(122, 'V202509150122', '2025-10-08 01:19:13.799850', 'boleta', 'completada', NULL, NULL, NULL, 7500.00, 1425.00, 8925.00, 'tarjeta_credito', NULL, 367, 7),
(123, 'V202505200123', '2025-10-08 01:19:13.824446', 'boleta', 'completada', NULL, NULL, NULL, 11200.00, 2128.00, 13328.00, 'transferencia', NULL, 123, 10),
(124, 'V202508230124', '2025-10-08 01:19:13.866015', 'factura', 'completada', NULL, NULL, NULL, 5900.00, 1121.00, 7021.00, 'transferencia', NULL, 409, 6),
(125, 'V202509250125', '2025-10-08 01:19:13.882873', 'boleta', 'completada', NULL, NULL, NULL, 1600.00, 304.00, 1904.00, 'tarjeta_debito', NULL, 374, 9),
(126, 'V202509090126', '2025-10-08 01:19:13.905238', 'factura', 'completada', NULL, NULL, NULL, 10500.00, 1995.00, 12495.00, 'tarjeta_debito', NULL, 376, 4),
(127, 'V202508250127', '2025-10-08 01:19:13.920980', 'boleta', 'completada', NULL, NULL, NULL, 7200.00, 1368.00, 8568.00, 'tarjeta_debito', NULL, 192, 7),
(128, 'V202508180128', '2025-10-08 01:19:13.932067', 'factura', 'completada', NULL, NULL, NULL, 8400.00, 1596.00, 9996.00, 'tarjeta_debito', NULL, 51, 12),
(129, 'V202509220129', '2025-10-08 01:19:13.960350', 'factura', 'completada', NULL, NULL, NULL, 3400.00, 646.00, 4046.00, 'tarjeta_debito', NULL, 314, 11),
(130, 'V202508200130', '2025-10-08 01:19:13.970576', 'boleta', 'completada', NULL, NULL, NULL, 6400.00, 1216.00, 7616.00, 'transferencia', NULL, 198, 12),
(131, 'V202505160131', '2025-10-08 01:19:14.002717', 'boleta', 'completada', NULL, NULL, NULL, 14500.00, 2755.00, 17255.00, 'tarjeta_credito', NULL, 235, 8),
(132, 'V202507200132', '2025-10-08 01:19:14.027312', 'factura', 'completada', NULL, NULL, NULL, 8700.00, 1653.00, 10353.00, 'transferencia', NULL, 341, 4),
(133, 'V202506010133', '2025-10-08 01:19:14.039693', 'factura', 'completada', NULL, NULL, NULL, 7300.00, 1387.00, 8687.00, 'efectivo', NULL, 121, 11),
(134, 'V202509030134', '2025-10-08 01:19:14.048098', 'boleta', 'completada', NULL, NULL, NULL, 17600.00, 3344.00, 20944.00, 'transferencia', NULL, 267, 8),
(135, 'V202509140135', '2025-10-08 01:19:14.063824', 'boleta', 'completada', NULL, NULL, NULL, 7400.00, 1406.00, 8806.00, 'tarjeta_debito', NULL, 122, 9),
(136, 'V202509190136', '2025-10-08 01:19:14.078597', 'boleta', 'completada', NULL, NULL, NULL, 3800.00, 722.00, 4522.00, 'efectivo', NULL, 79, 4),
(137, 'V202506100137', '2025-10-08 01:19:14.090563', 'factura', 'completada', NULL, NULL, NULL, 17500.00, 3325.00, 20825.00, 'tarjeta_debito', NULL, 382, 7),
(138, 'V202504120138', '2025-10-08 01:19:14.107228', 'boleta', 'completada', NULL, NULL, NULL, 17100.00, 3249.00, 20349.00, 'tarjeta_credito', NULL, 345, 8),
(139, 'V202510020139', '2025-10-08 01:19:14.126589', 'factura', 'completada', NULL, NULL, NULL, 3100.00, 589.00, 3689.00, 'efectivo', NULL, 140, 1),
(140, 'V202507070140', '2025-10-08 01:19:14.134010', 'factura', 'completada', NULL, NULL, NULL, 14300.00, 2717.00, 17017.00, 'tarjeta_debito', NULL, 224, 4),
(141, 'V202507250141', '2025-10-08 01:19:14.156227', 'factura', 'completada', NULL, NULL, NULL, 30200.00, 5738.00, 35938.00, 'efectivo', NULL, 223, 5),
(142, 'V202508080142', '2025-10-08 01:19:14.162566', 'factura', 'completada', NULL, NULL, NULL, 2500.00, 475.00, 2975.00, 'transferencia', NULL, 378, 6),
(143, 'V202507140143', '2025-10-08 01:19:14.165845', 'factura', 'completada', NULL, NULL, NULL, 16500.00, 3135.00, 19635.00, 'efectivo', NULL, 55, 9),
(144, 'V202505110144', '2025-10-08 01:19:14.179110', 'factura', 'completada', NULL, NULL, NULL, 11600.00, 2204.00, 13804.00, 'tarjeta_credito', NULL, 277, 6),
(145, 'V202505020145', '2025-10-08 01:19:14.189397', 'factura', 'completada', NULL, NULL, NULL, 8200.00, 1558.00, 9758.00, 'efectivo', NULL, 362, 10),
(146, 'V202505100146', '2025-10-08 01:19:14.215856', 'boleta', 'completada', NULL, NULL, NULL, 12800.00, 2432.00, 15232.00, 'tarjeta_credito', NULL, 14, 9),
(147, 'V202509020147', '2025-10-08 01:19:14.226180', 'boleta', 'completada', NULL, NULL, NULL, 3000.00, 570.00, 3570.00, 'efectivo', NULL, 378, 5),
(148, 'V202509230148', '2025-10-08 01:19:14.235370', 'factura', 'completada', NULL, NULL, NULL, 24100.00, 4579.00, 28679.00, 'transferencia', NULL, 17, 6),
(149, 'V202508200149', '2025-10-08 01:19:14.243522', 'factura', 'completada', NULL, NULL, NULL, 10000.00, 1900.00, 11900.00, 'tarjeta_credito', NULL, 166, 10),
(150, 'V202507230150', '2025-10-08 01:19:14.253787', 'boleta', 'completada', NULL, NULL, NULL, 22200.00, 4218.00, 26418.00, 'tarjeta_credito', NULL, 346, 8),
(151, 'V202507020151', '2025-10-08 01:19:14.263061', 'factura', 'completada', NULL, NULL, NULL, 2300.00, 437.00, 2737.00, 'transferencia', NULL, 261, 11),
(152, 'V202504290152', '2025-10-08 01:19:14.266738', 'boleta', 'completada', NULL, NULL, NULL, 5200.00, 988.00, 6188.00, 'tarjeta_credito', NULL, 440, 12),
(153, 'V202507240153', '2025-10-08 01:19:14.275461', 'factura', 'completada', NULL, NULL, NULL, 7600.00, 1444.00, 9044.00, 'transferencia', NULL, 377, 11),
(154, 'V202507280154', '2025-10-08 01:19:14.289059', 'factura', 'completada', NULL, NULL, NULL, 18400.00, 3496.00, 21896.00, 'tarjeta_credito', NULL, 424, 8),
(155, 'V202506160155', '2025-10-08 01:19:14.313629', 'boleta', 'completada', NULL, NULL, NULL, 19600.00, 3724.00, 23324.00, 'efectivo', NULL, 80, 7),
(156, 'V202506090156', '2025-10-08 01:19:14.361542', 'boleta', 'completada', NULL, NULL, NULL, 22800.00, 4332.00, 27132.00, 'tarjeta_credito', NULL, 351, 12),
(157, 'V202508060157', '2025-10-08 01:19:14.374837', 'factura', 'completada', NULL, NULL, NULL, 11800.00, 2242.00, 14042.00, 'transferencia', NULL, 256, 12),
(158, 'V202504170158', '2025-10-08 01:19:14.385115', 'boleta', 'completada', NULL, NULL, NULL, 20500.00, 3895.00, 24395.00, 'tarjeta_credito', NULL, 164, 9),
(159, 'V202509220159', '2025-10-08 01:19:14.408278', 'factura', 'completada', NULL, NULL, NULL, 16200.00, 3078.00, 19278.00, 'transferencia', NULL, 151, 11),
(160, 'V202507230160', '2025-10-08 01:19:14.427593', 'factura', 'completada', NULL, NULL, NULL, 20800.00, 3952.00, 24752.00, 'efectivo', NULL, 232, 11),
(161, 'V202504190161', '2025-10-07 16:43:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 4000.00, 760.00, 4760.00, 'efectivo', NULL, 211, 9),
(162, 'V202504180162', '2025-10-07 18:28:00.000000', 'factura', 'completada', NULL, NULL, NULL, 23200.00, 4408.00, 27608.00, 'transferencia', NULL, 474, 9),
(163, 'V202509040163', '2025-10-07 17:50:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 1600.00, 304.00, 1904.00, 'tarjeta_credito', NULL, 322, 10),
(164, 'V202506210164', '2025-10-07 14:45:00.000000', 'factura', 'completada', NULL, NULL, NULL, 9100.00, 1729.00, 10829.00, 'tarjeta_credito', NULL, 407, 11),
(165, 'V202508080165', '2025-10-07 17:05:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 3300.00, 627.00, 3927.00, 'transferencia', NULL, 438, 4),
(166, 'V202509130166', '2025-10-07 13:10:00.000000', 'factura', 'completada', NULL, NULL, NULL, 13200.00, 2508.00, 15708.00, 'tarjeta_debito', NULL, 285, 5),
(167, 'V202505060167', '2025-10-07 15:40:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 16200.00, 3078.00, 19278.00, 'efectivo', NULL, 267, 9),
(168, 'V202508190168', '2025-10-07 16:37:00.000000', 'factura', 'completada', NULL, NULL, NULL, 14500.00, 2755.00, 17255.00, 'transferencia', NULL, 407, 11),
(169, 'V202506030169', '2025-10-07 19:41:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 4600.00, 874.00, 5474.00, 'tarjeta_credito', NULL, 115, 9),
(170, 'V202505100170', '2025-10-07 19:35:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 9800.00, 1862.00, 11662.00, 'tarjeta_debito', NULL, 503, 10),
(171, 'V202504290171', '2025-10-07 14:04:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 10200.00, 1938.00, 12138.00, 'tarjeta_debito', NULL, 35, 7),
(172, 'V202508100172', '2025-10-07 16:19:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 4700.00, 893.00, 5593.00, 'tarjeta_credito', NULL, 480, 10),
(173, 'V202509300173', '2025-10-07 18:09:00.000000', 'factura', 'completada', NULL, NULL, NULL, 10700.00, 2033.00, 12733.00, 'transferencia', NULL, 457, 7),
(174, 'V202508270174', '2025-10-07 20:40:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 19900.00, 3781.00, 23681.00, 'tarjeta_credito', NULL, 73, 5),
(175, 'V202508040175', '2025-10-07 17:03:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 17600.00, 3344.00, 20944.00, 'tarjeta_credito', NULL, 247, 12),
(176, 'V202506050176', '2025-10-07 19:25:00.000000', 'factura', 'completada', NULL, NULL, NULL, 6000.00, 1140.00, 7140.00, 'transferencia', NULL, 407, 7),
(177, 'V202506060177', '2025-10-07 21:33:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 1600.00, 304.00, 1904.00, 'transferencia', NULL, 157, 8),
(178, 'V202506220178', '2025-10-07 21:41:00.000000', 'factura', 'completada', NULL, NULL, NULL, 1200.00, 228.00, 1428.00, 'efectivo', NULL, 371, 7),
(179, 'V202507100179', '2025-10-07 13:12:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 3600.00, 684.00, 4284.00, 'efectivo', NULL, 255, 10),
(180, 'V202504100180', '2025-10-07 20:27:00.000000', 'factura', 'completada', NULL, NULL, NULL, 7500.00, 1425.00, 8925.00, 'tarjeta_credito', NULL, 200, 10),
(181, 'V202505050181', '2025-10-07 14:15:00.000000', 'factura', 'completada', NULL, NULL, NULL, 11600.00, 2204.00, 13804.00, 'transferencia', NULL, 45, 8),
(182, 'V202506280182', '2025-10-07 19:46:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 32500.00, 6175.00, 38675.00, 'tarjeta_debito', NULL, 287, 4),
(183, 'V202505240183', '2025-10-07 17:39:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 3200.00, 608.00, 3808.00, 'transferencia', NULL, 91, 4),
(184, 'V202510070184', '2025-10-07 17:41:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 13100.00, 2489.00, 15589.00, 'efectivo', NULL, 460, 5),
(185, 'V202504180185', '2025-10-07 21:55:00.000000', 'factura', 'completada', NULL, NULL, NULL, 17300.00, 3287.00, 20587.00, 'tarjeta_credito', NULL, 376, 10),
(186, 'V202506040186', '2025-10-07 20:20:00.000000', 'factura', 'completada', NULL, NULL, NULL, 17600.00, 3344.00, 20944.00, 'transferencia', NULL, 469, 12),
(187, 'V202505270187', '2025-10-07 13:42:00.000000', 'factura', 'completada', NULL, NULL, NULL, 3600.00, 684.00, 4284.00, 'tarjeta_credito', NULL, 251, 9),
(188, 'V202506060188', '2025-10-07 11:10:00.000000', 'factura', 'completada', NULL, NULL, NULL, 6400.00, 1216.00, 7616.00, 'transferencia', NULL, 274, 6),
(189, 'V202508310189', '2025-10-07 20:12:00.000000', 'factura', 'completada', NULL, NULL, NULL, 4400.00, 836.00, 5236.00, 'tarjeta_debito', NULL, 73, 4),
(190, 'V202504190190', '2025-10-07 20:21:00.000000', 'factura', 'completada', NULL, NULL, NULL, 12500.00, 2375.00, 14875.00, 'tarjeta_debito', NULL, 97, 12),
(191, 'V202505130191', '2025-10-07 11:03:00.000000', 'factura', 'completada', NULL, NULL, NULL, 15400.00, 2926.00, 18326.00, 'tarjeta_debito', NULL, 440, 10),
(192, 'V202509050192', '2025-10-07 12:57:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 11400.00, 2166.00, 13566.00, 'tarjeta_debito', NULL, 151, 6),
(193, 'V202509290193', '2025-10-07 16:46:00.000000', 'factura', 'completada', NULL, NULL, NULL, 9500.00, 1805.00, 11305.00, 'tarjeta_credito', NULL, 455, 1),
(194, 'V202510020194', '2025-10-07 12:36:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 8000.00, 1520.00, 9520.00, 'efectivo', NULL, 88, 4),
(195, 'V202507160195', '2025-10-07 14:50:00.000000', 'factura', 'completada', NULL, NULL, NULL, 4000.00, 760.00, 4760.00, 'tarjeta_credito', NULL, 470, 9),
(196, 'V202507030196', '2025-10-07 20:14:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 10400.00, 1976.00, 12376.00, 'tarjeta_credito', NULL, 381, 1),
(197, 'V202510040197', '2025-10-07 15:37:00.000000', 'factura', 'completada', NULL, NULL, NULL, 5600.00, 1064.00, 6664.00, 'tarjeta_credito', NULL, 80, 4),
(198, 'V202509020198', '2025-10-07 21:43:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 10700.00, 2033.00, 12733.00, 'efectivo', NULL, 146, 5),
(199, 'V202507230199', '2025-10-07 21:36:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 4000.00, 760.00, 4760.00, 'transferencia', NULL, 263, 4),
(200, 'V202505060200', '2025-10-07 14:28:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 3800.00, 722.00, 4522.00, 'tarjeta_debito', NULL, 387, 7),
(201, 'V202508170201', '2025-10-07 17:34:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 2400.00, 456.00, 2856.00, 'tarjeta_credito', NULL, 337, 4),
(202, 'V202508040202', '2025-10-07 14:39:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 19700.00, 3743.00, 23443.00, 'tarjeta_debito', NULL, 78, 1),
(203, 'V202504130203', '2025-10-07 20:04:00.000000', 'factura', 'completada', NULL, NULL, NULL, 41400.00, 7866.00, 49266.00, 'efectivo', NULL, 79, 5),
(204, 'V202509190204', '2025-10-07 17:28:00.000000', 'factura', 'completada', NULL, NULL, NULL, 7400.00, 1406.00, 8806.00, 'tarjeta_debito', NULL, 387, 10),
(205, 'V202505020205', '2025-10-07 19:53:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 7200.00, 1368.00, 8568.00, 'transferencia', NULL, 473, 12),
(206, 'V202504270206', '2025-10-07 20:30:00.000000', 'factura', 'completada', NULL, NULL, NULL, 6000.00, 1140.00, 7140.00, 'transferencia', NULL, 319, 5),
(207, 'V202509040207', '2025-10-07 13:54:00.000000', 'factura', 'completada', NULL, NULL, NULL, 1200.00, 228.00, 1428.00, 'tarjeta_debito', NULL, 92, 6),
(208, 'V202507200208', '2025-10-07 15:11:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 9000.00, 1710.00, 10710.00, 'transferencia', NULL, 419, 1),
(209, 'V202509050209', '2025-10-07 19:48:00.000000', 'factura', 'completada', NULL, NULL, NULL, 11400.00, 2166.00, 13566.00, 'tarjeta_credito', NULL, 90, 12),
(210, 'V202506020210', '2025-10-07 12:14:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 14000.00, 2660.00, 16660.00, 'transferencia', NULL, 296, 10),
(211, 'V202507310211', '2025-10-07 19:05:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 15000.00, 2850.00, 17850.00, 'tarjeta_credito', NULL, 493, 10),
(212, 'V202510070212', '2025-10-07 13:09:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 7500.00, 1425.00, 8925.00, 'tarjeta_credito', NULL, 90, 6),
(213, 'V202510070213', '2025-10-07 11:22:00.000000', 'factura', 'completada', NULL, NULL, NULL, 5400.00, 1026.00, 6426.00, 'tarjeta_debito', NULL, 112, 6),
(214, 'V202510070214', '2025-10-07 12:51:00.000000', 'factura', 'completada', NULL, NULL, NULL, 11600.00, 2204.00, 13804.00, 'efectivo', NULL, 412, 7),
(215, 'V202510070215', '2025-10-07 18:15:00.000000', 'factura', 'completada', NULL, NULL, NULL, 22000.00, 4180.00, 26180.00, 'transferencia', NULL, 357, 4),
(216, 'V202510070216', '2025-10-07 16:59:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 9500.00, 1805.00, 11305.00, 'efectivo', NULL, 477, 5),
(217, 'V202510070217', '2025-10-07 15:05:00.000000', 'factura', 'completada', NULL, NULL, NULL, 4000.00, 760.00, 4760.00, 'transferencia', NULL, 333, 1),
(218, 'V202510070218', '2025-10-07 15:40:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 3600.00, 684.00, 4284.00, 'efectivo', NULL, 298, 7),
(219, 'V202510070219', '2025-10-07 19:21:00.000000', 'factura', 'completada', NULL, NULL, NULL, 7700.00, 1463.00, 9163.00, 'efectivo', NULL, 249, 4),
(220, 'V202510070220', '2025-10-07 19:26:00.000000', 'factura', 'completada', NULL, NULL, NULL, 9900.00, 1881.00, 11781.00, 'tarjeta_debito', NULL, 102, 5),
(221, 'V202510070221', '2025-10-07 18:04:00.000000', 'factura', 'completada', NULL, NULL, NULL, 11200.00, 2128.00, 13328.00, 'tarjeta_credito', NULL, 456, 4),
(222, 'V202510070222', '2025-10-07 14:24:00.000000', 'factura', 'completada', NULL, NULL, NULL, 4200.00, 798.00, 4998.00, 'efectivo', NULL, 386, 6),
(223, 'V202510070223', '2025-10-07 19:34:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 3000.00, 570.00, 3570.00, 'transferencia', NULL, 257, 1),
(224, 'V202510070224', '2025-10-07 19:03:00.000000', 'factura', 'completada', NULL, NULL, NULL, 12800.00, 2432.00, 15232.00, 'efectivo', NULL, 63, 7),
(225, 'V202510070225', '2025-10-07 13:10:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 14700.00, 2793.00, 17493.00, 'transferencia', NULL, 31, 6),
(226, 'V202510070226', '2025-10-07 21:58:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 4100.00, 779.00, 4879.00, 'transferencia', NULL, 59, 1),
(227, 'V202510080227', '2025-10-07 21:15:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 1000.00, 190.00, 1190.00, 'tarjeta_debito', NULL, 435, 5),
(228, 'V202510080228', '2025-10-07 20:18:00.000000', 'factura', 'completada', NULL, NULL, NULL, 13200.00, 2508.00, 15708.00, 'efectivo', NULL, 50, 5),
(229, 'V202510080229', '2025-10-07 13:28:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 4400.00, 836.00, 5236.00, 'tarjeta_debito', NULL, 289, 5),
(230, 'V202510080230', '2025-10-07 14:02:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 10800.00, 2052.00, 12852.00, 'transferencia', NULL, 158, 5),
(231, 'V202510080231', '2025-10-07 14:42:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 3700.00, 703.00, 4403.00, 'tarjeta_credito', NULL, 48, 1),
(232, 'V202510080232', '2025-10-07 15:15:00.000000', 'factura', 'completada', NULL, NULL, NULL, 1200.00, 228.00, 1428.00, 'efectivo', NULL, 372, 1),
(233, 'V202510080233', '2025-10-07 14:17:00.000000', 'factura', 'completada', NULL, NULL, NULL, 600.00, 114.00, 714.00, 'transferencia', NULL, 507, 5),
(234, 'V202510080234', '2025-10-07 15:13:00.000000', 'factura', 'completada', NULL, NULL, NULL, 8000.00, 1520.00, 9520.00, 'efectivo', NULL, 252, 5),
(235, 'V202510070235', '2025-10-07 15:40:00.000000', 'factura', 'completada', NULL, NULL, NULL, 3600.00, 684.00, 4284.00, 'tarjeta_debito', NULL, 492, 5),
(236, 'V202510070236', '2025-10-07 21:06:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 1100.00, 209.00, 1309.00, 'efectivo', NULL, 472, 1),
(237, 'V202510070237', '2025-10-07 18:55:00.000000', 'factura', 'completada', NULL, NULL, NULL, 2000.00, 380.00, 2380.00, 'tarjeta_debito', NULL, 472, 1),
(238, 'V202510070238', '2025-10-07 12:49:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 6400.00, 1216.00, 7616.00, 'efectivo', NULL, 358, 4),
(239, 'V202510070239', '2025-10-07 21:59:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 800.00, 152.00, 952.00, 'efectivo', NULL, 69, 1),
(240, 'V202510070240', '2025-10-07 12:14:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 1600.00, 304.00, 1904.00, 'transferencia', NULL, 496, 5),
(241, 'V202510070241', '2025-10-07 16:22:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 4500.00, 855.00, 5355.00, 'tarjeta_debito', NULL, 350, 1),
(242, 'V202510070242', '2025-10-07 18:26:00.000000', 'factura', 'completada', NULL, NULL, NULL, 800.00, 152.00, 952.00, 'transferencia', NULL, 8, 4),
(243, 'V202510070243', '2025-10-07 20:06:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 1000.00, 190.00, 1190.00, 'tarjeta_debito', NULL, 218, 1),
(244, 'V202510070244', '2025-10-07 21:35:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 8000.00, 1520.00, 9520.00, 'tarjeta_debito', NULL, 161, 5),
(245, 'V202510070245', '2025-10-07 13:12:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 1200.00, 228.00, 1428.00, 'efectivo', NULL, 377, 1),
(246, 'V202510070246', '2025-10-07 19:27:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 3100.00, 589.00, 3689.00, 'transferencia', NULL, 383, 1),
(247, 'V202510070247', '2025-10-07 18:50:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 3100.00, 589.00, 3689.00, 'tarjeta_credito', NULL, 166, 4),
(248, 'V202510070248', '2025-10-07 18:32:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 2600.00, 494.00, 3094.00, 'tarjeta_debito', NULL, 300, 4),
(249, 'V202510070249', '2025-10-07 14:36:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 600.00, 114.00, 714.00, 'transferencia', NULL, 105, 1),
(250, 'V202510070250', '2025-10-07 21:17:00.000000', 'factura', 'completada', NULL, NULL, NULL, 6500.00, 1235.00, 7735.00, 'transferencia', NULL, 19, 1),
(251, 'V202510070251', '2025-10-07 15:29:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 1500.00, 285.00, 1785.00, 'transferencia', NULL, 33, 1),
(252, 'V202510070252', '2025-10-07 17:35:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 6000.00, 1140.00, 7140.00, 'transferencia', NULL, 108, 5),
(253, 'V202510070253', '2025-10-07 13:01:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 1500.00, 285.00, 1785.00, 'tarjeta_debito', NULL, 394, 5),
(254, 'V202510070254', '2025-10-07 18:06:00.000000', 'factura', 'completada', NULL, NULL, NULL, 4000.00, 760.00, 4760.00, 'transferencia', NULL, 458, 5),
(255, 'V202510070255', '2025-10-07 20:52:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 7000.00, 1330.00, 8330.00, 'tarjeta_debito', NULL, 27, 1),
(256, 'V202510070256', '2025-10-07 19:56:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 2000.00, 380.00, 2380.00, 'transferencia', NULL, 75, 1),
(257, 'V202510070257', '2025-10-07 17:37:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 9200.00, 1748.00, 10948.00, 'transferencia', NULL, 112, 5),
(258, 'V202510070258', '2025-10-07 17:51:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 300.00, 57.00, 357.00, 'efectivo', NULL, 180, 1),
(259, 'V202510070259', '2025-10-07 16:17:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 10200.00, 1938.00, 12138.00, 'efectivo', NULL, 96, 5),
(260, 'V202510070260', '2025-10-07 11:14:00.000000', 'factura', 'completada', NULL, NULL, NULL, 11600.00, 2204.00, 13804.00, 'transferencia', NULL, 452, 1),
(261, 'V20251007999', '2025-10-07 18:49:00.000000', 'boleta', 'completada', NULL, NULL, NULL, 1000.00, 190.00, 1190.00, 'efectivo', NULL, 377, 1),
(263, 'V-20251007-001', '2025-10-08 01:42:37.441983', 'boleta', 'completada', NULL, NULL, NULL, 215000.00, 40850.00, 255850.00, 'efectivo', NULL, 516, 1),
(264, 'V-20251007-002', '2025-10-08 01:42:37.459084', 'boleta', 'completada', NULL, NULL, NULL, 1600000.00, 304000.00, 1904000.00, 'efectivo', NULL, 515, 1),
(265, 'V-20251007-003', '2025-10-08 01:42:37.471181', 'boleta', 'completada', NULL, NULL, NULL, 240000.00, 45600.00, 285600.00, 'efectivo', NULL, 2, 1),
(266, 'V-20251007-004', '2025-10-08 01:42:37.475164', 'boleta', 'completada', NULL, NULL, NULL, 660000.00, 125400.00, 785400.00, 'efectivo', NULL, 515, 1),
(267, 'V-20251007-005', '2025-10-08 01:42:37.482322', 'boleta', 'completada', NULL, NULL, NULL, 445000.00, 84550.00, 529550.00, 'efectivo', NULL, 2, 1),
(268, 'V-20251007-006', '2025-10-08 01:42:37.489386', 'boleta', 'completada', NULL, NULL, NULL, 1280000.00, 243200.00, 1523200.00, 'efectivo', NULL, 506, 1),
(269, 'V-20251007-007', '2025-10-08 01:42:37.494947', 'boleta', 'completada', NULL, NULL, NULL, 1065000.00, 202350.00, 1267350.00, 'efectivo', NULL, 506, 1),
(270, 'V-20251007-008', '2025-10-08 01:42:37.499335', 'boleta', 'completada', NULL, NULL, NULL, 660000.00, 125400.00, 785400.00, 'efectivo', NULL, 506, 1),
(271, 'V-20251007-009', '2025-10-08 01:42:37.505472', 'boleta', 'completada', NULL, NULL, NULL, 700000.00, 133000.00, 833000.00, 'efectivo', NULL, 506, 1),
(272, 'V-20251007-010', '2025-10-08 01:42:37.517504', 'boleta', 'completada', NULL, NULL, NULL, 170000.00, 32300.00, 202300.00, 'efectivo', NULL, 4, 1),
(273, 'V-20251007-011', '2025-10-08 01:42:37.520085', 'boleta', 'completada', NULL, NULL, NULL, 320000.00, 60800.00, 380800.00, 'efectivo', NULL, 4, 1),
(274, 'V-20251007-012', '2025-10-08 01:42:37.523157', 'boleta', 'completada', NULL, NULL, NULL, 465000.00, 88350.00, 553350.00, 'efectivo', NULL, 505, 1),
(275, 'V-20251004-001', '2025-10-08 01:42:37.529511', 'boleta', 'completada', NULL, NULL, NULL, 360000.00, 68400.00, 428400.00, 'efectivo', NULL, 1, 1),
(276, 'V-20251005-001', '2025-10-08 01:42:37.532671', 'boleta', 'completada', NULL, NULL, NULL, 365000.00, 69350.00, 434350.00, 'efectivo', NULL, 516, 1),
(277, 'V-20251006-001', '2025-10-08 01:42:37.542092', 'boleta', 'completada', NULL, NULL, NULL, 565000.00, 107350.00, 672350.00, 'efectivo', NULL, 515, 1),
(278, 'V202510070001', '2025-10-08 01:43:26.658883', 'boleta', 'completada', NULL, NULL, NULL, 52500.00, 9975.00, 62475.00, 'efectivo', '', 118, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_app_usuario`
--
ALTER TABLE `auth_app_usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_app_usuario_groups`
--
ALTER TABLE `auth_app_usuario_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_app_usuario_groups_usuario_id_group_id_f6b18eac_uniq` (`usuario_id`,`group_id`),
  ADD KEY `auth_app_usuario_groups_group_id_80dd3f8c_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_app_usuario_user_permissions`
--
ALTER TABLE `auth_app_usuario_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_app_usuario_user_pe_usuario_id_permission_id_360acddb_uniq` (`usuario_id`,`permission_id`),
  ADD KEY `auth_app_usuario_use_permission_id_38185ec5_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `djangoVerVictorMondaca_clientes`
--
ALTER TABLE `djangoVerVictorMondaca_clientes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rut` (`rut`);

--
-- Indices de la tabla `djangoVerVictorMondaca_productos`
--
ALTER TABLE `djangoVerVictorMondaca_productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_app_usuario_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `ventas_app_controldia`
--
ALTER TABLE `ventas_app_controldia`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `fecha` (`fecha`),
  ADD KEY `ventas_app_controldi_usuario_apertura_id_e4d32699_fk_auth_app_` (`usuario_apertura_id`),
  ADD KEY `ventas_app_controldi_usuario_cierre_id_56d51aad_fk_auth_app_` (`usuario_cierre_id`);

--
-- Indices de la tabla `ventas_app_itemventa`
--
ALTER TABLE `ventas_app_itemventa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ventas_app_itemventa_producto_id_c0c1811d_fk_djangoVer` (`producto_id`),
  ADD KEY `ventas_app_itemventa_venta_id_31545ea6_fk_ventas_app_venta_id` (`venta_id`);

--
-- Indices de la tabla `ventas_app_resumendiario`
--
ALTER TABLE `ventas_app_resumendiario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `fecha` (`fecha`);

--
-- Indices de la tabla `ventas_app_venta`
--
ALTER TABLE `ventas_app_venta`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numero_venta` (`numero_venta`),
  ADD KEY `ventas_app_venta_cliente_id_c8dc870b_fk_djangoVer` (`cliente_id`),
  ADD KEY `ventas_app_venta_vendedor_id_75899db1_fk_auth_app_usuario_id` (`vendedor_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_app_usuario`
--
ALTER TABLE `auth_app_usuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `auth_app_usuario_groups`
--
ALTER TABLE `auth_app_usuario_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_app_usuario_user_permissions`
--
ALTER TABLE `auth_app_usuario_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `djangoVerVictorMondaca_clientes`
--
ALTER TABLE `djangoVerVictorMondaca_clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=517;

--
-- AUTO_INCREMENT de la tabla `djangoVerVictorMondaca_productos`
--
ALTER TABLE `djangoVerVictorMondaca_productos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=133;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `ventas_app_controldia`
--
ALTER TABLE `ventas_app_controldia`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `ventas_app_itemventa`
--
ALTER TABLE `ventas_app_itemventa`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=777;

--
-- AUTO_INCREMENT de la tabla `ventas_app_resumendiario`
--
ALTER TABLE `ventas_app_resumendiario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `ventas_app_venta`
--
ALTER TABLE `ventas_app_venta`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=279;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_app_usuario_groups`
--
ALTER TABLE `auth_app_usuario_groups`
  ADD CONSTRAINT `auth_app_usuario_gro_usuario_id_c61065ad_fk_auth_app_` FOREIGN KEY (`usuario_id`) REFERENCES `auth_app_usuario` (`id`),
  ADD CONSTRAINT `auth_app_usuario_groups_group_id_80dd3f8c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_app_usuario_user_permissions`
--
ALTER TABLE `auth_app_usuario_user_permissions`
  ADD CONSTRAINT `auth_app_usuario_use_permission_id_38185ec5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_app_usuario_use_usuario_id_c909008a_fk_auth_app_` FOREIGN KEY (`usuario_id`) REFERENCES `auth_app_usuario` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_app_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `auth_app_usuario` (`id`);

--
-- Filtros para la tabla `ventas_app_controldia`
--
ALTER TABLE `ventas_app_controldia`
  ADD CONSTRAINT `ventas_app_controldi_usuario_apertura_id_e4d32699_fk_auth_app_` FOREIGN KEY (`usuario_apertura_id`) REFERENCES `auth_app_usuario` (`id`),
  ADD CONSTRAINT `ventas_app_controldi_usuario_cierre_id_56d51aad_fk_auth_app_` FOREIGN KEY (`usuario_cierre_id`) REFERENCES `auth_app_usuario` (`id`);

--
-- Filtros para la tabla `ventas_app_itemventa`
--
ALTER TABLE `ventas_app_itemventa`
  ADD CONSTRAINT `ventas_app_itemventa_producto_id_c0c1811d_fk_djangoVer` FOREIGN KEY (`producto_id`) REFERENCES `djangoVerVictorMondaca_productos` (`id`),
  ADD CONSTRAINT `ventas_app_itemventa_venta_id_31545ea6_fk_ventas_app_venta_id` FOREIGN KEY (`venta_id`) REFERENCES `ventas_app_venta` (`id`);

--
-- Filtros para la tabla `ventas_app_venta`
--
ALTER TABLE `ventas_app_venta`
  ADD CONSTRAINT `ventas_app_venta_cliente_id_c8dc870b_fk_djangoVer` FOREIGN KEY (`cliente_id`) REFERENCES `djangoVerVictorMondaca_clientes` (`id`),
  ADD CONSTRAINT `ventas_app_venta_vendedor_id_75899db1_fk_auth_app_usuario_id` FOREIGN KEY (`vendedor_id`) REFERENCES `auth_app_usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
