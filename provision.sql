-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 24, 2023 at 08:31 AM
-- Server version: 10.4.11-MariaDB  
-- PHP Version: 7.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medical`
--

-- --------------------------------------------------------

--
-- Table structure for table `addmp`
--

CREATE TABLE `addmp` (
  `sno` int(11) NOT NULL,
  `item` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addmp`
--

INSERT INTO `addmp` (`sno`, `item`) VALUES
(1, 'Rice'),
(2, 'Sugar'),
(3, 'Salt'),
(4, 'Cooking oil'),
(5, 'Jaggery'),
(6, 'Egg'),
(7, 'wheat'),
(8, 'flour');

-- --------------------------------------------------------

--
-- Table structure for table `addpd`
--

CREATE TABLE `addpd` (
  `sno` int(11) NOT NULL,
  `product` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addpd`
--

INSERT INTO `addpd` (`sno`, `product`) VALUES
(1, 'Biscuits'),
(2, 'Harpic'),
(3, 'garnier hair colour'),
(4, 'Noodles');

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

CREATE TABLE `logs` (
  `id` int(11) NOT NULL,
  `mid` int(11) NOT NULL,
  `action` varchar(500) NOT NULL,
  `date` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `logs`
--

INSERT INTO `logs` (`id`, `mid`, `action`, `date`) VALUES
(1, 101, ' INSERTED', '2025-01-25 12:54:41'),
(2, 102, ' DELETED', '2025-01-25 12:57:48');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  
  `id` int(11) NOT NULL,
  `arrival` DATE NOT NULL,
  `name` varchar(100) NOT NULL,
  `items` varchar(500) NOT NULL,
  `products` varchar(500) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mid` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Triggers `orders`
--
DELIMITER $$
CREATE TRIGGER `Delete` BEFORE DELETE ON `orders` FOR EACH ROW INSERT INTO Logs VALUES(null,OLD.mid,' DELETED',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `Insert` AFTER INSERT ON `orders` FOR EACH ROW INSERT INTO Logs VALUES(null,NEW.mid,' INSERTED',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `Update` AFTER UPDATE ON `orders` FOR EACH ROW INSERT INTO Logs VALUES(null,NEW.mid,' UPDATED',NOW())
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `mid` int(11) NOT NULL,
  `items_name` varchar(100) NOT NULL,
  `owner_name` varchar(100) NOT NULL,
  `phone_no` varchar(20) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`mid`, `items_name`, `owner_name`, `phone_no`, `address`) VALUES
(103, 'Sugar', 'kiran', '8796541230', 'Bangalore');

--
-- Indexes for dumped tables
--  

--
-- Indexes for table `addmp`
--
ALTER TABLE `addmp`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `addpd`
--
ALTER TABLE `addpd`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`mid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addmp`
--
ALTER TABLE `addmp`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `addpd`
--
ALTER TABLE `addpd`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `mid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1002;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
