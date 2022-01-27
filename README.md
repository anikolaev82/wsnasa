# Библиотека для сервисов NASA


После установки пакета, необходимо произвести настройку.  

>from nasaapi.config import Config  
>Config(token='TOKENNASA',storage=ClassStorage, connection_string='conn_str')  

## Token
Получить ключ можно здесь https://api.nasa.gov/  
или использовать DEMO_KEY  

## Storage
Определяет способ хранинения кэша.  
В наличии 2 способа: StorageMemory, StorageDatabase.  
Для создания собственного способа, используется интерфейс  

>from nasaapi.entity.abclass.abcstorage import AbcStorage


## connestion string
Указывается если выбрано хранилище StorageDatabase

