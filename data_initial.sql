-- MySQL dump 10.13  Distrib 8.0.38, for macos14 (arm64)
--
-- Host: 127.0.0.1    Database: mycooking
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add category',6,'add_category'),(22,'Can change category',6,'change_category'),(23,'Can delete category',6,'delete_category'),(24,'Can view category',6,'view_category'),(25,'Can add recipe',7,'add_recipe'),(26,'Can change recipe',7,'change_recipe'),(27,'Can delete recipe',7,'delete_recipe'),(28,'Can view recipe',7,'view_recipe'),(29,'Can add ingredient',8,'add_ingredient'),(30,'Can change ingredient',8,'change_ingredient'),(31,'Can delete ingredient',8,'delete_ingredient'),(32,'Can view ingredient',8,'view_ingredient'),(33,'Can add recipe ingredient',9,'add_recipeingredient'),(34,'Can change recipe ingredient',9,'change_recipeingredient'),(35,'Can delete recipe ingredient',9,'delete_recipeingredient'),(36,'Can view recipe ingredient',9,'view_recipeingredient'),(37,'Can add user',10,'add_user'),(38,'Can change user',10,'change_user'),(39,'Can delete user',10,'delete_user'),(40,'Can view user',10,'view_user'),(41,'Can add review',11,'add_review'),(42,'Can change review',11,'change_review'),(43,'Can delete review',11,'delete_review'),(44,'Can view review',11,'view_review');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-03-30 03:37:14.778549','11','Gạo lứt',1,'[{\"added\": {}}]',8,4),(2,'2025-03-30 03:37:24.006153','11','Gạo thường',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(3,'2025-03-30 03:37:31.829918','11','Bắp Mỹ',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(4,'2025-03-30 03:37:42.507731','12','Đậu cove',1,'[{\"added\": {}}]',8,4),(5,'2025-03-30 03:38:15.537119','13','Trứng gà',1,'[{\"added\": {}}]',8,4),(6,'2025-03-30 03:38:20.806023','13','Cá',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(7,'2025-03-30 03:38:31.640923','13','Cà chua',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(8,'2025-03-30 03:38:54.610154','13','Thịt cua',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(9,'2025-03-30 03:38:57.916632','13','Thịt',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(10,'2025-03-30 03:39:15.338691','13','Chuối',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(11,'2025-03-30 03:39:25.842680','13','Bạch Tuộc',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(12,'2025-03-30 03:39:29.643194','13','Tôm',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(13,'2025-03-30 03:39:58.370660','14','Bạch tuộc',1,'[{\"added\": {}}]',8,4),(14,'2025-03-30 03:40:14.844215','14','Bánh phở',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(15,'2025-03-30 03:40:36.203625','14','Thơm',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(16,'2025-03-30 03:40:39.721670','14','Táo',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(17,'2025-03-30 03:41:27.352843','15','Cá',1,'[{\"added\": {}}]',8,4),(18,'2025-03-30 03:41:47.019571','15','Trứng gà',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,4),(19,'2025-03-30 03:42:02.048445','16','Cá',1,'[{\"added\": {}}]',8,4),(20,'2025-03-30 03:42:14.319921','17','Mì gói',1,'[{\"added\": {}}]',8,4),(21,'2025-03-30 03:42:25.924758','18','Cơm trắng',1,'[{\"added\": {}}]',8,4),(22,'2025-03-30 03:42:31.088736','19','Cơm gạo lứt',1,'[{\"added\": {}}]',8,4),(23,'2025-03-30 03:46:24.667526','20','Sữa tươi không đường',1,'[{\"added\": {}}]',8,4),(24,'2025-03-30 03:46:39.324610','21','Nước cốt dừa',1,'[{\"added\": {}}]',8,4),(25,'2025-03-30 03:47:12.753881','22','Đá bi',1,'[{\"added\": {}}]',8,4),(26,'2025-03-30 03:52:48.249622','23','Trân châu khô',1,'[{\"added\": {}}]',8,4),(27,'2025-03-30 03:52:57.951701','24','Topping Cream',1,'[{\"added\": {}}]',8,4),(28,'2025-03-30 03:53:06.251409','25','Thịt nạc',1,'[{\"added\": {}}]',8,4),(29,'2025-03-30 03:53:13.703370','26','Sườn que',1,'[{\"added\": {}}]',8,4);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'recipes','category'),(8,'recipes','ingredient'),(7,'recipes','recipe'),(9,'recipes','recipeingredient'),(11,'reviews','review'),(5,'sessions','session'),(10,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-03-28 06:57:33.622548'),(2,'contenttypes','0002_remove_content_type_name','2025-03-28 06:57:33.632548'),(3,'auth','0001_initial','2025-03-28 06:57:33.670626'),(4,'auth','0002_alter_permission_name_max_length','2025-03-28 06:57:33.681266'),(5,'auth','0003_alter_user_email_max_length','2025-03-28 06:57:33.684348'),(6,'auth','0004_alter_user_username_opts','2025-03-28 06:57:33.686307'),(7,'auth','0005_alter_user_last_login_null','2025-03-28 06:57:33.688122'),(8,'auth','0006_require_contenttypes_0002','2025-03-28 06:57:33.688512'),(9,'auth','0007_alter_validators_add_error_messages','2025-03-28 06:57:33.690433'),(10,'auth','0008_alter_user_username_max_length','2025-03-28 06:57:33.692083'),(11,'auth','0009_alter_user_last_name_max_length','2025-03-28 06:57:33.693851'),(12,'auth','0010_alter_group_name_max_length','2025-03-28 06:57:33.698346'),(13,'auth','0011_update_proxy_permissions','2025-03-28 06:57:33.700675'),(14,'auth','0012_alter_user_first_name_max_length','2025-03-28 06:57:33.703161'),(15,'users','0001_initial','2025-03-28 06:57:33.747436'),(16,'admin','0001_initial','2025-03-28 06:57:33.769703'),(17,'admin','0002_logentry_remove_auto_add','2025-03-28 06:57:33.772549'),(18,'admin','0003_logentry_add_action_flag_choices','2025-03-28 06:57:33.774793'),(19,'recipes','0001_initial','2025-03-28 06:57:33.807293'),(20,'reviews','0001_initial','2025-03-28 06:57:33.821367'),(21,'reviews','0002_initial','2025-03-28 06:57:33.834830'),(22,'sessions','0001_initial','2025-03-28 06:57:33.840468'),(23,'recipes','0002_recipe_cook_time2','2025-03-28 19:30:05.202951'),(24,'recipes','0003_remove_recipe_cook_time2','2025-03-28 19:30:45.984781'),(25,'recipes','0004_recipe_author_alter_recipe_category_and_more','2025-03-29 01:33:26.415443'),(26,'recipes','0005_alter_recipe_image','2025-03-29 02:05:26.524045');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `recipes_category`
--

LOCK TABLES `recipes_category` WRITE;
/*!40000 ALTER TABLE `recipes_category` DISABLE KEYS */;
INSERT INTO `recipes_category` VALUES (1,'Món chay'),(2,'Món mặn'),(4,'Món nước'),(5,'Món nướng'),(3,'Món tráng miệng');
/*!40000 ALTER TABLE `recipes_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `recipes_ingredient`
--

LOCK TABLES `recipes_ingredient` WRITE;
/*!40000 ALTER TABLE `recipes_ingredient` DISABLE KEYS */;
INSERT INTO `recipes_ingredient` VALUES (11,'Bắp Mỹ'),(10,'Bột mì'),(16,'Cá'),(4,'Cà rốt'),(19,'Cơm gạo lứt'),(18,'Cơm trắng'),(22,'Đá bi'),(12,'Đậu cove'),(3,'Đậu hũ'),(8,'Gừng'),(6,'Hành tím'),(5,'Khoai tây'),(17,'Mì gói'),(21,'Nước cốt dừa'),(9,'Sữa đặc'),(20,'Sữa tươi không đường'),(26,'Sườn que'),(14,'Táo'),(2,'Thịt bò'),(1,'Thịt gà'),(25,'Thịt nạc'),(7,'Tỏi'),(13,'Tôm'),(24,'Topping Cream'),(23,'Trân châu khô'),(15,'Trứng gà');
/*!40000 ALTER TABLE `recipes_ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `recipes_recipe`
--

LOCK TABLES `recipes_recipe` WRITE;
/*!40000 ALTER TABLE `recipes_recipe` DISABLE KEYS */;
INSERT INTO `recipes_recipe` VALUES (1,'Đậu hũ chiên','Miếng đậu hũ mềm mịn bên trong, giòn rụm bên ngoài, thường được chiên vàng đều và dùng kèm với nước chấm chua ngọt hoặc mắm tỏi','[{\"step\": 1, \"instruction\": \"C\\u1eaft \\u0111\\u1eadu h\\u0169 th\\u00e0nh mi\\u1ebfng nh\\u1ecf.\"}, {\"step\": 2, \"instruction\": \"Chi\\u00ean gi\\u00f2n \\u0111\\u1eadu h\\u0169 v\\u1edbi d\\u1ea7u \\u0103n.\"}]',10,'recipe_images/dau_hu_chien.jpg','2025-03-29 02:12:59.969270','2025-03-29 02:12:59.969287',1,1),(2,'Canh gà hầm sâm','Món ăn bổ dưỡng kết hợp giữa thịt gà thơm mềm và nhân sâm, hầm chung với các loại thảo dược, tạo nên nước dùng thanh, bổ và giàu dinh dưỡng.','[{\"step\": 1, \"instruction\": \"H\\u1ea7m g\\u00e0 v\\u1edbi nh\\u00e2n s\\u00e2m, t\\u00e1o \\u0111\\u1ecf, v\\u00e0 g\\u1eebng.\"}]',60,'recipe_images/canh_ga_ham_sam.jpg','2025-03-29 02:12:59.970898','2025-03-29 02:12:59.970907',2,1),(3,'Bò lúc lắc','Thịt bò mềm, đậm đà gia vị, được xào chín tới cùng rau củ như ớt chuông và hành tây, mang hương vị thơm ngon và cân bằng.','[{\"step\": 1, \"instruction\": \"X\\u00e0o th\\u1ecbt b\\u00f2 v\\u1edbi \\u1edbt chu\\u00f4ng v\\u00e0 h\\u00e0nh t\\u00e2y.\"}]',20,'recipe_images/bo_luc_lac.jpg','2025-03-29 02:12:59.972508','2025-03-29 02:12:59.972519',2,1),(4,'Súp bí đỏ','Thịt bò mềm, đậm đà gia vị, được xào chín tới cùng rau củ như ớt chuông và hành tây, mang hương vị thơm ngon và cân bằng.','[{\"step\": 1, \"instruction\": \"N\\u1ea5u b\\u00ed \\u0111\\u1ecf v\\u1edbi s\\u1eefa t\\u01b0\\u01a1i r\\u1ed3i xay nhuy\\u1ec5n.\"}]',30,'recipe_images/sup_bi_do.jpg','2025-03-29 02:12:59.974029','2025-03-29 02:12:59.974042',4,1),(5,'Cơm gạo lứt trộn','Cơm gạo lứt trộn là món ăn vừa bổ dưỡng vừa ngon miệng, rất thích hợp cho chị em ăn kiêng. Cơm gạo lứt sau khi nấu ngon, thơm dịu. Cơm kết hợp với các loại rau củ tươi ngọt thanh mát bổ sung thêm nhiều lớp hương vị cho món cơm thuần túy khiến món ăn trở nên hấp dẫn hơn bao giờ hết.','[{\"step\": 1, \"instruction\": \"Gạo lứt vo sạch, ngâm với 200ml nước trong vòng 20 phút.\"}, {\"step\": 2, \"instruction\": \"Tỏi, hành tím băm nhuyễn.\"}, {\"step\": 3, \"instruction\": \"Cà rốt cắt hạt lựu, Bắp Mỹ tách lấy hạt.Đậu tước sơ cắt nhỏ 5mm.\"}, {\"step\": 4, \"instruction\": \"Nấm đông cô tươi bỏ gốc, rửa nhanh dưới vòi nước lạnh, cắt hạt lựu.\"}, {\"step\": 5, \"instruction\": \"Cho gạo và các nguyên liệu vào nồi cơm điện, nêm cùng 1/2m nước tương, 1/2m Hạt nêm Aji-ngon. Nấm vào nấu chín.\"}, {\"step\": 6, \"instruction\": \"Sau khi chín, cho hành lá vào trộn đều.Cho hành tỏi phi vào trộn đều cùng cơm.\"}, {\"step\": 7, \"instruction\": \"Trộn đều cơm với hỗn hợp rau củ, trang trí thêm ngò rí, ăn kèm nước tương.\"}]',41,'recipe_images/com-gao-lut-tron.jpg','2025-03-30 03:19:18.192089','2025-03-30 07:40:20.706439',2,4),(6,'Cá bống trứng kho tiêu','Cá bống trứng kho tiêu là món ăn nhiều dưỡng chất vì gan cá chứa nhiều Omega 3 có tác dụng tốt cho thị lực và bổ thần kinh. Món ăn cũng rất phù hợp cho người ăn kiêng giảm khối mỡ thừa cho cơ thể. Món cá kho ngon với cá còn nguyên vẹn, nước kho sánh sệt màu vàng nâu, vị đậm đà, thơm mùi hành, tiêu.','[{\"step\": 1, \"instruction\": \"Mỡ heo cắt nhỏ. Hành lá rửa sạch, phần đầu trắng đập dập, cắt nhuyễn, phần lá cắt nhỏ.\"}, {\"step\": 2, \"instruction\": \"Cá bống trứng làm sạch, rửa qua nước lạnh, để thật ráo, ướp với đầu hành trắng băm, 1/2m tiêu, 1/2m muối, 1m đường, \"}, {\"step\": 3, \"instruction\": \"1m Hạt nêm Aji-ngon , 1M nước mắm, 1M tương ớt.\"}, {\"step\": 4, \"instruction\": \"Thắng mỡ đến khi vàng giòn, vớt tóp mỡ ra, giữ mỡ lại trong nồi đất, cho 1M đường vào, thắng caramel đến khi có màu nâu đẹp mắt, cho tiếp 1M tỏi băm vào đảo đều.\"}, {\"step\": 5, \"instruction\": \"Sau đó cho cá vào đảo nhanh và nhẹ tay để cá thấm caramel và săn lại. Nêm vào 1m Hạt nêm Aji-ngon® HEO, 1M nước mắm để dậy mùi thơm, nước sánh lại thì cho tốp mỡ vào, đảo đều.\\\\r\\\\nThêm ớt hiểm và nước nóng vào vừa xấp mặt cá, giảm nhỏ lửa, thỉnh thoảng lắc nhẹ nồi để cá và thịt thấm gia vị đều, nước gần cạn hết thì tắt lửa.\"}, {\"step\": 6, \"instruction\": \"Rắc tiêu và hành lá lên cá cho thơm. Dùng nóng với cơm trắng.\"}]',30,'recipe_images/ca-bong-trung-kho-tieu.jpg.jpg','2025-03-30 03:35:53.855817','2025-03-30 03:35:53.855849',2,4),(7,'Trà sữa kem Matcha','Trà sữa kem matcha với lớp kem bông mềm mại, thơm mùi trà xanh. Trà sữa đượm vị gạo rang và ngọt vừa phải. Kết hợp với topping gạo lức giòn giòn vui miệng. Một món thức uống thích hợp cho những ai là fan của matcha đích thực!! Thử ngay nào.','[{\"step\": 1, \"instruction\": \"Đánh kem: đánh bông hỗn hợp topping gồm kem topping, sữa tươi, nước cốt dừa và 1m Trà sữa Matcha gạo rang. Đánh đến khi hỗn hợp đặc lại, bông lên và mịn là được\"}, {\"step\": 2, \"instruction\": \"Pha Trà sữa Matcha gạo rang theo hướng dẫn trên bao bì.\"}, {\"step\": 3, \"instruction\": \"Cho đá vào ly, rót trà sữa, thêm kem matcha lên trên, cuối cùng rắc cốm gạo lứt và thưởng thức.\"}]',10,'recipe_images/cach-lam-matcha-da-xay.jpg','2025-03-30 03:51:34.986650','2025-03-30 03:51:34.986684',4,4);
/*!40000 ALTER TABLE `recipes_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `recipes_recipeingredient`
--

LOCK TABLES `recipes_recipeingredient` WRITE;
/*!40000 ALTER TABLE `recipes_recipeingredient` DISABLE KEYS */;
INSERT INTO `recipes_recipeingredient` VALUES (1,'200g',3,1),(2,'1 con',1,2),(3,'1 nhánh',8,2),(4,'300g',2,3),(5,'200g',5,4),(8,'5g',6,6),(9,'5g',7,6),(10,'250ml',20,7),(11,'20g',9,7),(14,'10g',7,5),(15,'200g',1,5);
/*!40000 ALTER TABLE `recipes_recipeingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `reviews_review`
--

LOCK TABLES `reviews_review` WRITE;
/*!40000 ALTER TABLE `reviews_review` DISABLE KEYS */;
INSERT INTO `reviews_review` VALUES (1,5,'Món ăn rất ngon!','2025-03-29 02:12:59.984548',1,2),(2,4,'Hầm lâu quá, nhưng hương vị tuyệt vời!','2025-03-29 02:12:59.986231',2,3),(3,3,'Bò hơi dai.','2025-03-29 02:12:59.987618',3,2),(4,4,'Cũng được','2025-03-30 08:50:43.382678',3,4),(5,4,'Chưa từng ăn món nào mà nó ngon như món này','2025-03-30 08:55:52.435502',5,4);
/*!40000 ALTER TABLE `reviews_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,'pbkdf2_sha256$870000$MDZr1AU9YgioVxnphBm6yI$awzJ20xY9sIfzXVucU6Ui4WVDH/+3/CEBaL+eF2O3HQ=',NULL,0,'admin','','',0,1,'2025-03-29 02:12:59.386931','admin@example.com',1),(2,'pbkdf2_sha256$870000$O5uVCxRf7rKoM2hhZ4VHRk$E+cT8OD3NPfAZnqRGR6q+RydsQxlEnS14ShNOGpqxZU=',NULL,0,'user1','','',0,1,'2025-03-29 02:12:59.577105','user1@example.com',0),(3,'pbkdf2_sha256$870000$xmASwnsHWLPsLMPX3BMZyE$pNofkj5hnKmRzWR3xc7hurXSjzbxjV5vieg6Vtl+CXA=',NULL,0,'user2','','',0,1,'2025-03-29 02:12:59.761644','user2@example.com',0),(4,'pbkdf2_sha256$870000$JSe5l9Vw70fvzz1iT84xy1$CcT8ybD1gaelNHlxtYAwn7Re/IF5hD3Rw2pG7KEzM58=','2025-03-30 03:46:17.493807',1,'abc','','',1,1,'2025-03-29 16:21:17.266933','abc@gmail.com',0);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-30 16:07:59
