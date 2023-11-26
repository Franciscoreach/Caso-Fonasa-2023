-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-11-2023 a las 19:01:01
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fonasa_bd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consulta_paciente`
--

CREATE TABLE `consulta_paciente` (
  `idConsulta` int(5) NOT NULL,
  `noHistoriaClinica` int(5) NOT NULL,
  `nombrePaciente` varchar(100) NOT NULL,
  `edad` int(3) NOT NULL,
  `prioridad` int(4) NOT NULL,
  `riesgo` double NOT NULL,
  `nombreEsp` varchar(100) NOT NULL,
  `fechaConsulta` timestamp NOT NULL DEFAULT current_timestamp(),
  `tipoConsulta` varchar(25) NOT NULL,
  `estado` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `noHistoriaClinica` int(5) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `edad` int(3) NOT NULL,
  `prioridad` int(5) NOT NULL,
  `riesgo` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `panciano`
--

CREATE TABLE `panciano` (
  `noHistoriaClinica` int(5) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `edad` int(3) NOT NULL,
  `tieneDieta` tinyint(1) NOT NULL,
  `prioridad` int(4) NOT NULL,
  `riesgo` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pjoven`
--

CREATE TABLE `pjoven` (
  `noHistoriaClinica` int(5) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `edad` int(2) NOT NULL,
  `fumador` tinyint(1) NOT NULL,
  `prioridad` int(4) NOT NULL,
  `riesgo` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pninno`
--

CREATE TABLE `pninno` (
  `noHistoriaClinica` int(5) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `edad` int(2) NOT NULL,
  `estatura` int(3) NOT NULL,
  `peso` int(2) NOT NULL,
  `relacionPesoEstatura` int(4) DEFAULT NULL,
  `riesgo` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `consulta_paciente`
--
ALTER TABLE `consulta_paciente`
  ADD PRIMARY KEY (`idConsulta`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`noHistoriaClinica`);

--
-- Indices de la tabla `panciano`
--
ALTER TABLE `panciano`
  ADD PRIMARY KEY (`noHistoriaClinica`);

--
-- Indices de la tabla `pjoven`
--
ALTER TABLE `pjoven`
  ADD PRIMARY KEY (`noHistoriaClinica`);

--
-- Indices de la tabla `pninno`
--
ALTER TABLE `pninno`
  ADD PRIMARY KEY (`noHistoriaClinica`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `consulta_paciente`
--
ALTER TABLE `consulta_paciente`
  MODIFY `idConsulta` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
