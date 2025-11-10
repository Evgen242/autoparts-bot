--
-- PostgreSQL database dump
--

\restrict EVUCSRQ4WMt3ZoESnzTiGVLpT24zebIVLMrhGnzL7Ck01uTl34GHNYd33cFY91b

-- Dumped from database version 14.19 (Ubuntu 14.19-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.19 (Ubuntu 14.19-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: autoparts; Type: TABLE; Schema: public; Owner: autoparts_user
--

CREATE TABLE public.autoparts (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    car_brand character varying(50),
    car_model character varying(50),
    part_number character varying(50),
    quantity integer,
    price double precision,
    location character varying(100),
    description character varying(500),
    created_at timestamp without time zone
);


ALTER TABLE public.autoparts OWNER TO autoparts_user;

--
-- Name: autoparts_id_seq; Type: SEQUENCE; Schema: public; Owner: autoparts_user
--

CREATE SEQUENCE public.autoparts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.autoparts_id_seq OWNER TO autoparts_user;

--
-- Name: autoparts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: autoparts_user
--

ALTER SEQUENCE public.autoparts_id_seq OWNED BY public.autoparts.id;


--
-- Name: autoparts id; Type: DEFAULT; Schema: public; Owner: autoparts_user
--

ALTER TABLE ONLY public.autoparts ALTER COLUMN id SET DEFAULT nextval('public.autoparts_id_seq'::regclass);


--
-- Data for Name: autoparts; Type: TABLE DATA; Schema: public; Owner: autoparts_user
--

COPY public.autoparts (id, name, car_brand, car_model, part_number, quantity, price, location, description, created_at) FROM stdin;
1	Лобовое стекло	Skoda	Octavia A5	23378-883738	5	5000	Стеллаж 10	Новое, оригинал	2025-09-19 15:23:33.326173
2	Тормозной диск	Skoda	Octavia A5	377372-83883	3	300	Стеллаж 3	Новый, оригинал	2025-09-19 15:26:39.939783
3	Суппорт	Skoda	Octavia A5	377372-83883	3	350	Стеллаж 3	Новый, оригинал	2025-09-19 15:27:23.918253
4	Фара	Skoda	Octavia A5	377372-66373	3	450	Стеллаж 3	Новый, оригинал	2025-09-19 15:28:00.801477
5	Тормозной подшипник	Skoda	Octavia A5	377372-83883	3	100	Стеллаж 4	Новый, оригинал	2025-09-19 15:28:22.517185
6	Ось суппорта	Skoda	Octavia A5	377372-83883	3	150	Стеллаж 5	Новый, оригинал	2025-09-19 15:28:46.254302
7	Шина	Skoda	Octavia A5	377372-8554	3	505	Стеллаж 3	Новый, оригинал	2025-09-19 15:30:51.732937
8	Дверь левая	Skoda	Octavia A5	377372-83883	3	300	Стеллаж 3	Новый, оригинал	2025-09-19 15:32:21.474646
9	Дверь правая	Skoda	Octavia A5	377372-83883	3	400	Стеллаж 3	Новый, оригинал	2025-09-19 15:32:40.897446
10	Дверь задняя левая	Skoda	Octavia A5	377372-83883	3	600	Стеллаж 9	Новый, оригинал	2025-09-19 15:33:06.416951
11	Дверь задняя правая	Skoda	Octavia A5	377372-83826364	3	550	Стеллаж 7	Новый, оригинал	2025-09-19 15:33:37.901973
12	Крышка багажника	Skoda	Octavia A5	377372-83883	3	460	Стеллаж 11	Новый, оригинал	2025-09-19 15:34:13.421177
13	Капот	Skoda	Octavia A5	377372-83883	5	489	Стеллаж 15	Новый, оригинал	2025-09-19 15:34:41.913863
14	Руль	Skoda	Octavia A5	377372-8322982	3	150	Стеллаж 17	Новый, оригинал	2025-09-19 15:35:10.471201
15	ГРМ	Skoda	Octavia A5	377372-83455665	3	9000	Стеллаж 15	Новый, оригинал	2025-09-19 15:50:14.804051
16	ДСГ	Skoda	Octavia A5	377372-484883	11	750	Стеллаж 3	Новый, оригинал	2025-09-19 15:50:43.05563
17	Диск сцепления	Skoda	Octavia A5	377372-8398282	3	587	Стеллаж 21	Новый, оригинал	2025-09-19 15:51:35.166239
18	Трос сцепления	Skoda	Octavia A5	377372-838678655	3	687	Стеллаж 22	Новый, оригинал	2025-09-19 15:53:41.43791
19	Защита ДВС	Skoda	OctaviaA5	83773747-3883&	11	250	17	Новый, оригинал	2025-09-19 20:35:00.568367
20	Кожух сцепления	Skoda	OctaviaA5	83773747-38344	15	250	17	Новый, оригинал	2025-09-19 20:35:26.700173
21	Армотизатор задний	Skoda	OctaviaA5	83773747-3884848	53	250	14	Новый, оригинал	2025-09-19 20:36:01.768935
22	Ароматизатор задний левый	Skoda	OctaviaA5	83773747-172	17	2737	51	Новый, оригинал	2025-09-19 20:37:31.377832
23	Защита стекла	Skoda	OctaviaA5	83773747-388	18	250	56	Новый, оригинал	2025-09-19 20:37:55.791132
24	Поддон	Skoda	OctaviaA5	83773747-3883&	570	67	Новый, оригинал		2025-09-19 20:38:34.78365
25	Лампочка поворотника задняя левая	Skoda	OctaviaA5	83773747-388	18	250	56	Новый, оригинал	2025-09-19 20:44:32.283038
26	Лампочка поворотника задняя правая	Skoda	OctaviaA5	83773747-388	18	250	56	Новый, оригинал	2025-09-19 20:44:56.314623
27	Лапочка поворотника переднего левая	Skoda	OctaviaA5	83773747-388	18	250	56	Новый, оригинал лампочка поворотника переднего левая	2025-09-19 20:45:33.828157
28	Лампочка поворотника переднего правая	Skoda	OctaviaA5	83773747-388	18	250	56	Новый, оригинал	2025-09-19 20:45:53.475531
29	Гидроусилитель руля	Skoda	OctaviaA5	83773747-38848383	67	250	56Защита стекла	Skoda	2025-09-19 20:46:29.43527
30	Суппорт задний	Skoda	OctaviaA5	83773747-388383	50	250	56	Новый, оригинал	2025-09-19 20:46:55.23958
31	Супорт задний правый	Skoda	OctaviaA5	83773747-388	18	250	50	Новый, оригинал	2025-09-19 20:47:15.157137
32	Супорт передний правый	Skoda	OctaviaA5	83773747-388	18	250	50	Новый, оригинал	2025-09-19 20:47:33.100527
33	Супорт передний правый	Skoda	OctaviaA5	83773747-38889292	18	250	50	Новый, оригинал	2025-09-19 20:47:56.351316
34	Стекло заднее	Skoda	OctaviaA5	83773747-388	60	300	56	Новый, оригинал	2025-09-19 20:48:25.943663
35	Стекло переднее	Skoda	OctaviaA5	83773747-388883	18	300	60	Новый, оригинал	2025-09-19 20:48:52.748431
36	Диск 17R	Skoda	OctaviaA5	83773747-388	500	65	Новый, оригинал		2025-09-19 20:49:30.1837
37	Диск 17R передний левый	Skoda	OctaviaA5	83773747-388773	500	65	Новый, оригинал		2025-09-19 20:49:50.958093
38	Диск 17R передний правый	Skoda	OctaviaA5	83773747-3888282	500	65	Новый, оригинал		2025-09-19 20:50:08.016044
39	Диск 17R задний левый	Skoda	OctaviaA5	83773747-388222	500	65	Новый, оригинал		2025-09-19 20:50:23.586164
40	Диск 17R задний правый	Skoda	OctaviaA5	83773747-38822	500	65	Новый, оригинал		2025-09-19 20:50:39.280541
41	Люди к тормозной	Skoda	OctaviaA5	83773747-388333	500	70	Новый, оригинал		2025-09-19 20:52:44.462319
42	Диск  тормозной передний левый	Skoda	OctaviaA5	83773747-388222	500	70	Новый, оригинал		2025-09-19 20:53:04.903059
43	Диск тормозной задний правый	Skoda	OctaviaA5	83773747-388	500	70	Новый, оригинал		2025-09-19 20:53:25.101999
44	Диск задний левый	Skoda	OctaviaA5	83773747-38833	500	70	Новый, оригинал		2025-09-19 20:53:43.842546
45	Диск 17R	Skoda	OctaviaA5	83773747-388	500	65	Новый, оригинал		2025-09-19 20:53:50.107815
46	Диск сцепления	Skoda	OctaviaA5	83773747-38883883	500	100	Новый, оригинал		2025-09-19 20:54:14.038644
47	Диск  вакуумный	Skoda	OctaviaA5	83773747-388	500	99	Новый, оригинал		2025-09-19 20:54:29.389872
48	Диск варочный	Skoda	OctaviaA5	83773747-388777	500	77	Новый, оригинал		2025-09-19 20:54:47.499861
49	Домкрат	Skoda	OctaviaA5	83773747-38877733	500	78	Новый, оригинал		2025-09-19 20:55:22.834264
50	Домра	Skoda	OctaviaA5	83773747-38877777	500	78	Новый, оригинал		2025-09-19 20:55:42.523193
51	Антенна	Skoda	OctaviaA5	83773747-388732883	11	78	Новый, оригинал		2025-09-20 13:56:39.44308
52	Антенна	Skoda	OctaviaA5	83773747-388732883	11	78	Новый, оригинал		2025-09-22 05:45:02.778142
53	Диск  CD	Skoda	OctaviaA5	8377372773-7474	500	99	Новый, оригинал		2025-09-24 12:54:15.825942
54	Болт R17	Skoda	OctaviaA5	83773747-388	10000	100	Новый, оригинал		2025-09-24 12:55:33.315917
55	Чехлы салона	Skoda	OctaviaA5	83773747-388	500	0	Стеллаж 73	Новый, оригинал	2025-09-24 12:57:42.53947
56	ДВГ 2.0 DTI	Toyota	Camry	2735-773	345	2000	Стеллаж B2	Новый	2025-09-25 21:42:06.922756
57	ДВГ 2.0 DTI	Opel	Vectors	2735-773	345	2000	Стеллаж B2	Новый	2025-09-25 21:42:39.51089
58	ДВГ 2.0 DTI	Nissan	Zhuk	2735-773	345	2000	Стеллаж B2	Новый	2025-09-25 21:43:10.991982
59	ДВГ 2.0 DTI	VW	Passat	2735-773	345	2000	Стеллаж B2	Новый	2025-09-25 21:43:43.561006
60	ДВГ 2.0 DTI	Jeep	Camry	2735-773	345	0	Стеллаж B2	Новый	2025-09-25 21:58:12.515416
61	ДВГ 1.9 Sri	Toyota	Camry	2735-773	345	500	Стеллаж B2	Новый	2025-09-30 07:25:17.600152
62	Электродвигатель	Tesla	Model S	145776-6765	30	10000	Стеллаж B21	Новый	2025-09-30 07:25:43.033561
63	Электродвигатель	Tesla	Model 3	145776	30	15000	Стеллаж B22	Новый	2025-09-30 07:26:08.063331
64	Электродвигатель	Voyager	Free pro	145776-556	45	9000	Стеллаж B23	Новый	2025-09-30 07:27:23.77397
65	Электродвигатель	Voyah	Free pro	145776-6654	30	9000	Стеллаж B25	Новый	2025-09-30 07:28:32.85996
66	Электродвигатель	Voyah	Free pro	145776-6654	30	9000	Стеллаж B25	Новый	2025-10-02 07:44:54.650615
67	Электродвигатель	Voyah	Free pro	145776-6654	30	9000	Стеллаж B25	Новый	2025-10-14 08:43:46.631506
68	Электродвигатель	Voyah	Free pro	145776-6654	30	9000	Стеллаж B25	Новый	2025-10-24 12:31:11.973527
69	Электродвигатель	Tesla	Free pro	145776-66345	30	9000	Стеллаж B21	Новый	2025-10-27 14:52:07.111471
\.


--
-- Name: autoparts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: autoparts_user
--

SELECT pg_catalog.setval('public.autoparts_id_seq', 101, true);


--
-- Name: autoparts autoparts_pkey; Type: CONSTRAINT; Schema: public; Owner: autoparts_user
--

ALTER TABLE ONLY public.autoparts
    ADD CONSTRAINT autoparts_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA public TO autoparts_user;


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES  TO autoparts_user;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO autoparts_user;


--
-- PostgreSQL database dump complete
--

\unrestrict EVUCSRQ4WMt3ZoESnzTiGVLpT24zebIVLMrhGnzL7Ck01uTl34GHNYd33cFY91b

