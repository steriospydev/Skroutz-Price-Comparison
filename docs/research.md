### Find url detailed page product that you wish to track the price
### Search for html components and identifiers:
- div.spec-groups
1. CPU: item(0)
   - CPU: 2nd dl->dd ( e.g: Ryzen 5) (1)
2. Freq:
   - 4th dl->dd (e.g: 3 Ghz)(3)
3. B.Screen: item(1)
   - diagonal : 2nd dl->dd (e.g: 15,6)(1)
   - ratio : 3rd dl->dd (e.g:1920x1080)(2)
4. C.RAM:item(2)
   -	capacity :	1st dl->dd ( e.g:	 8 GB)(0)
   - type : 2nd dl->dd ( e.g:	 DDR4)(1)
5. D. GPU: item(3)
   - model : 2nd dl->dd(1)
6. E.Hard Disk: item(4)
	- type : 1st dl->dd (e.g: SSD)(0)
    - capacity:	2nd dl->dd ( e.g: 512GB)(1)
      -	OR ul.two-columns-list	->	all li
7. Price
   - loading-btn .btn-green	->span.default	->	span	->strong
	
### Sample python code:
- info[items[0].h3.text] = items[0].select('dl>dd')[1].text + ' ' + items[0].select('dl>dd')[3].text
- info[items[1].h3.text] = items[1].select('dl>dd')[1].text + ' ' + items[1].select('dl>dd')[2].text
- info[items[2].h3.text] = items[2].select('dl>dd')[0].text + ' ' + items[2].select('dl>dd')[1].text
- info[items[3].h3.text] = items[3].select('dl>dd')[1].text 
- info[items[4].h3.text] = items[4].select('dl>dd')[1].text + ' ' + items[4].select('dl>dd')[0].text
