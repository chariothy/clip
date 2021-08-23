# clip
Mini clip board for curl &amp; webpage.

## Put something on it (simply return digital id)

1. Put message
   
    `curl localhost:8000 -F t="Some text"`

1. Put file

    `curl localhost:8000 -F f=@c:/some-file`


## Get something from it ({id} is what we just returned from Copy)
1. Get message
   
    `curl localhost:8000/{id}`

1. Get file

    `curl -o file_name.ext localhost:8000/{id}`



# TODO:
1. Add md5 to check if things already exists
2. Check if exceed container