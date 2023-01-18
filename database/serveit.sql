CREATE DATABASE  IF NOT EXISTS `serveit` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `serveit`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: serveit
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `college`
--

DROP TABLE IF EXISTS `college`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college` (
  `collegeCode` varchar(10) NOT NULL,
  `collegeName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`collegeCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college`
--

LOCK TABLES `college` WRITE;
/*!40000 ALTER TABLE `college` DISABLE KEYS */;
INSERT INTO `college` VALUES ('CASS','College of Arts & Social Science'),('CCS','College of Computer Studies'),('CEBA','College of Economics, Business & Account'),('CED','College of Education'),('COET','College of Engineering & Technology'),('CON','College of Nursing'),('CSM','College of Science & Mathematics');
/*!40000 ALTER TABLE `college` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `courseCode` varchar(10) NOT NULL,
  `courseName` varchar(100) DEFAULT NULL,
  `collegeCode` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`courseCode`),
  KEY `FK_collegeCode_idx` (`collegeCode`),
  CONSTRAINT `FK_collegeCode` FOREIGN KEY (`collegeCode`) REFERENCES `college` (`collegeCode`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES ('BAENG','Bachelor of Arts in English','CASS'),('BAFIL','Bachelor of Arts in Filipino','CASS'),('BAHIS','Bachelor of Arts in History','CASS'),('BAPSC','Bachelor of Arts in Political Science','CASS'),('BSA','Bachelor of Science in Accountancy','CEBA'),('BSBA','Bachelor of Science in Business Administration','CEBA'),('BSBIO','Bachelor of Science in Biology','CSM'),('BSCE','Bachelor of Science in Civil Engineering','COET'),('BSCEE','Bachelor of Science in Ceramics Engineering','COET'),('BSCH','Bachelor of Science in Chemistry','CSM'),('BSCHE','Bachelor of Science in Chemical Engineering','COET'),('BSCOE','Bachelor of Science in Computer Engineering','COET'),('BSCS','Bachelor of Science in Computer Science','CCS'),('BSEBI','Bachelor of Secondary Education Biology','CED'),('BSECE','Bachelor of Science in Electronics and Communications Engineering','COET'),('BSECH','Bachelor of Secondary Education Chemistry','CED'),('BSECT','Bachelor of Science in Electronics and Computer Technology','CCS'),('BSEE','Bachelor of Science in Electrical Engineering','COET'),('BSEEN','Bachelor of Secondary Education English','CED'),('BSEGS','Bachelor of Secondary Education General Science','CED'),('BSEMT','Bachelor of Secondary Education Mathematics','CED'),('BSEPE','Bachelor of Secondary Education MAPEH','CED'),('BSEPH','Bachelor of Secondary Education Physics','CED'),('BSESH','Bachelor of Secondary Education Science and Health','CED'),('BSETL','Bachelor of Secondary Education TLE','CED'),('BSHRM','Bachelor of Science in Hotel and Restaurant Management','CEBA'),('BSIED','Bachelor of Science in Industrial Education Drafting','CED'),('BSIS','Bachelor of Science in Information Systems','CCS'),('BSIT','Bachelor of Science in Information Technology','CCS'),('BSMAT','Bachelor of Science in Mathematics','CSM'),('BSME','Bachelor of Science in Mechanical Engineering','COET'),('BSMET','Bachelor of Science in Metallurgical Engineering','COET'),('BSMNE','Bachelor of Science in Mining Engineering','COET'),('BSN','Bachelor of Science in Nursing','CON'),('BSPHY','Bachelor of Science in Physics','CSM'),('BSPSY','Bachelor of Science in Psychology','CASS'),('BSSTT','Bachelor of Science in Statistics','CSM'),('GENED','General Education Program','CASS');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `payment_id` varchar(50) NOT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  `mode_of_payment` varchar(50) NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `FK_user_id-users_idx` (`user_id`),
  CONSTRAINT `FK_user_id-payment` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requests` (
  `request_id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `service_code` varchar(50) NOT NULL,
  `order_status` varchar(50) NOT NULL,
  `order_date` varchar(50) NOT NULL,
  `date_accepted` varchar(45) DEFAULT NULL,
  `date_completed` varchar(50) DEFAULT NULL,
  `user_id_accept` varchar(50) DEFAULT NULL,
  `payment_id` varchar(50) NOT NULL,
  `location` varchar(100) NOT NULL,
  PRIMARY KEY (`request_id`),
  KEY `FK_user_id-users_idx` (`user_id`),
  KEY `request_services_code_idx` (`service_code`),
  KEY `FK_payment_id-payment_idx` (`payment_id`),
  CONSTRAINT `FK_payment_id-payment` FOREIGN KEY (`payment_id`) REFERENCES `payments` (`payment_id`),
  CONSTRAINT `FK_service_code-services` FOREIGN KEY (`service_code`) REFERENCES `services` (`service_code`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `FK_user_id-users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `FK_user_id_accept-users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_gcash`
--

DROP TABLE IF EXISTS `service_gcash`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_gcash` (
  `gcash_id` varchar(50) NOT NULL,
  `gcash_type` varchar(45) NOT NULL,
  `amount` varchar(45) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `service_code` varchar(45) NOT NULL,
  PRIMARY KEY (`gcash_id`),
  KEY `FK_service_code-gcash_idx` (`service_code`),
  CONSTRAINT `FK_service_code-gcash` FOREIGN KEY (`service_code`) REFERENCES `services` (`service_code`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_gcash`
--

LOCK TABLES `service_gcash` WRITE;
/*!40000 ALTER TABLE `service_gcash` DISABLE KEYS */;
/*!40000 ALTER TABLE `service_gcash` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_print`
--

DROP TABLE IF EXISTS `service_print`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_print` (
  `print_id` varchar(50) NOT NULL,
  `service_code` varchar(45) DEFAULT NULL,
  `file` varchar(100) DEFAULT NULL,
  `number_of_copies` varchar(50) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`print_id`),
  KEY `FK_service_code-print_idx` (`service_code`),
  CONSTRAINT `FK_service_code-print` FOREIGN KEY (`service_code`) REFERENCES `services` (`service_code`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_print`
--

LOCK TABLES `service_print` WRITE;
/*!40000 ALTER TABLE `service_print` DISABLE KEYS */;
/*!40000 ALTER TABLE `service_print` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `service_code` varchar(50) NOT NULL,
  `service_name` varchar(50) NOT NULL,
  PRIMARY KEY (`service_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` varchar(10) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `college` varchar(100) DEFAULT NULL,
  `course` varchar(100) DEFAULT NULL,
  `idnumber` varchar(45) DEFAULT NULL,
  `userImg` varchar(255) DEFAULT NULL,
  `contact_number` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `idnumber_UNIQUE` (`idnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('SDID0001','badingka??','Gabriel00!','Gabriel','Lawrence','male','gabbypaylaga1@gmail.com','CCS','BSIT','2019-2130',NULL,NULL),('SDID0002','badingka?','Gabriel00!','Badingka','Badingjd','male','badingka@gmail.com','CCS','BSIT','2019-2222',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-19  2:58:03
