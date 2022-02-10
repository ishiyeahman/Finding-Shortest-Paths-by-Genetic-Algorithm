# Finding-Shortest-Paths-by-Genetic-Algorithm

## For What 

I am interested in Optimazation Problem, Especially Shortest Path Problem. 

So, I tried to find shortest paths by  [Genetic Algorithm (GA)](https://en.wikipedia.org/wiki/Genetic_algorithm).(ja:[遺伝的アルゴリズム](https://ja.wikipedia.org/wiki/%E9%81%BA%E4%BC%9D%E7%9A%84%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0))


GA is sometimes used as the method to solve 
[Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
(ja: [巡回セールスマン問題](https://ja.wikipedia.org/wiki/%E5%B7%A1%E5%9B%9E%E3%82%BB%E3%83%BC%E3%83%AB%E3%82%B9%E3%83%9E%E3%83%B3%E5%95%8F%E9%A1%8C)).


## How to Use
I coded this program for the class in NITK.
You can read the report I submited .(out/GAapp.pdf)

I've not still coded for public version whoever can run.
I'll try soon!

## Example 

These are the intial generaion of a path route, around Hitoyoshi city, Kumamoto pref.

There are various pattern of path route to destination from source.

* source : lower left
* destination : upper right

<img src="(https://user-images.githubusercontent.com/72023343/153434609-b876194e-ff4a-4bed-877e-b261b6bb7635.png" width="100" height="100">

![init-0(0 061068121083690155)](https://user-images.githubusercontent.com/72023343/153434609-b876194e-ff4a-4bed-877e-b261b6bb7635.png)
![init-1(0 2091804519224655)](https://user-images.githubusercontent.com/72023343/153436764-213a65f8-7855-4f8f-addc-dec98e6172c9.png)
![init-2(0 052003483511486724)](https://user-images.githubusercontent.com/72023343/153436766-7dcb520d-98b4-4f4a-b7c7-a14cbd2a3712.png)
![init-3(0 10844913213324008)](https://user-images.githubusercontent.com/72023343/153436767-8001c1cb-5a8d-46f6-9f84-f696eb9facbe.png)
![init-8(0 11187178872301763)](https://user-images.githubusercontent.com/72023343/153436768-62290c18-1d98-4705-b44e-4dc673c63ce0.png)
![init-9(0 19068306890727252)](https://user-images.githubusercontent.com/72023343/153436770-c3f7d88b-095d-4faa-a24e-c5aaa6434ec1.png)

Finally, we can get it might be shotest path, but this isn't best though.
![30-0(0 025296474360838005)](https://user-images.githubusercontent.com/72023343/153437800-3e75a151-04d2-42cd-84f5-38b34bc34832.png)


This is might be good solution. This path is created by other initial generation. Actually, this path isn't best path, but it was extremely shorter than first generarion.

![30-0(0 014954716402028959)](https://user-images.githubusercontent.com/72023343/153438390-e0dd7e5e-ab81-4f46-829f-9736976a4702.png)


