
# Eskom REST API loadshedding documentation

## 1\. Get Status

`Get status of loadshedding` [_Check if there is any loadshedding_]

* * *

### Calling Parameters (Input)

<table>

<thead>

<tr>

<th style="text-align:left">Parameter</th>

<th style="text-align:left">Mode</th>

<th style="text-align:left">Description</th>

<th style="text-align:left">example values</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left">`NULL`</td>

<td style="text-align:left">NULL</td>

<td style="text-align:left">NULL</td>

<td style="text-align:left">NULL</td>

</tr>

</tbody>

</table>

### Interface Address

https://loadshedding.eskom.co.za/LoadShedding/GetStatus

### Request Method

*   HTTP
*   GET
*   POST

### Response Parameters (Output)

<table>

<thead>

<tr>

<th style="text-align:left">Parameter</th>

<th style="text-align:left">Mode</th>

<th style="text-align:left">Description</th>

<th style="text-align:left">example values</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left">`integer`</td>

<td style="text-align:left">int</td>

<td style="text-align:left">Https</td>

<td style="text-align:left">1</td>

</tr>

</tbody>

</table>

### Example:

*   Returned data:
    *   Is a single character/value. If less than 1 then discard. If more or equal subtract 1 for the current stage.
*   Example:
    *   1 = No load shedding, 2 = Stage 1, 3 = Stage 2, 4 = Stage 3, 5 = Stage 4

### Response Result Example

    //1 means no loadshedding
    1

* * *

* * *

* * *

## 2\. Get Municipalities

`Get Municipalities` [_get the municipalities using the API_]

* * *

### Calling Parameters (Input)

<table>

<thead>

<tr>

<th style="text-align:left">Parameter</th>

<th style="text-align:left">Mode</th>

<th style="text-align:left">Description</th>

<th style="text-align:left">example values</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left">`Id=`</td>

<td style="text-align:left">int</td>

<td style="text-align:left">municipalitie id</td>

<td style="text-align:left">9</td>

</tr>

</tbody>

</table>

### Province IDs:

*   1 = Eastern Cape
*   2 = Free State
*   3 = Gauteng
*   4 = KwaZulu-Natal
*   5 = Limpopo
*   6 = Mpumalanga
*   7 = North West
*   8 = Northern Cape
*   9 = Western Cape

### Interface Address

https://loadshedding.eskom.co.za/LoadShedding/GetMunicipalities/?Id=4

### Request Method

*   HTTP
*   GET
*   POST

### Response Parameters (Output)

<table>

<thead>

<tr>

<th style="text-align:left">Parameter</th>

<th style="text-align:left">Mode</th>

<th style="text-align:left">Description</th>

<th style="text-align:left">example values</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left">`Selected`</td>

<td style="text-align:left">boolean</td>

<td style="text-align:left">is selected</td>

<td style="text-align:left">false</td>

</tr>

<tr>

<td style="text-align:left">`Text`</td>

<td style="text-align:left">String</td>

<td style="text-align:left">name</td>

<td style="text-align:left">Beaufort West</td>

</tr>

<tr>

<td style="text-align:left">`Value`</td>

<td style="text-align:left">String</td>

<td style="text-align:left">value</td>

<td style="text-align:left">336</td>

</tr>

</tbody>

</table>

### Response Result Example

    [
       {
          "Selected":false,
          "Text":"Beaufort West",
          "Value":"336"
       }
    ]

* * *

* * *

* * *

## 3\. Get Surburb Data

`Get The Surburb Data` [_get the surburb data using the API_]

* * *

### Calling Parameters (Input)

<table>

<thead>

<tr>

<th style="text-align:left">Parameter</th>

<th style="text-align:left">Mode</th>

<th style="text-align:left">Description</th>

<th style="text-align:left">example values</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left">`pageSize`</td>

<td style="text-align:left">int</td>

<td style="text-align:left">size of the page</td>

<td style="text-align:left">100</td>

</tr>

<tr>

<td style="text-align:left">`pageNum`</td>

<td style="text-align:left">int</td>

<td style="text-align:left">number of pages</td>

<td style="text-align:left">1</td>

</tr>

<tr>

<td style="text-align:left">`id`</td>

<td style="text-align:left">int</td>

<td style="text-align:left">id</td>

<td style="text-align:left">336</td>

</tr>

</tbody>

</table>

### Interface Address

http://loadshedding.eskom.co.za/LoadShedding/GetSurburbData/?pageSize=100&pageNum=1&id=340

### Example:

*   List suburbs of municipality:
*   Call: http://loadshedding.eskom.co.za/LoadShedding/GetSurburbData/?pageSize=100&pageNum=1&id=<municipality_id>
*   Example (Municipality = Overstrand): http://loadshedding.eskom.co.za/LoadShedding/GetSurburbData/?pageSize=100&pageNum=1&id=10254
    *   include the pageSize and pageNum parameters or the call will fail.

### Request Method

*   HTTP
*   GET
*   POST

### Response Parameters (Output)

<table>

<thead>

<tr>

<th style="text-align:left">Parameter</th>

<th style="text-align:left">Mode</th>

<th style="text-align:left">Description</th>

<th style="text-align:left">example values</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left">`id`</td>

<td style="text-align:left">String</td>

<td style="text-align:left">id</td>

<td style="text-align:left">63591</td>

</tr>

<tr>

<td style="text-align:left">`text`</td>

<td style="text-align:left">String</td>

<td style="text-align:left">name</td>

<td style="text-align:left">Alexandra</td>

</tr>

<tr>

<td style="text-align:left">`Tot`</td>

<td style="text-align:left">int</td>

<td style="text-align:left">total</td>

<td style="text-align:left">271</td>

</tr>

</tbody>

</table>

*   If Tot is 0 then there won't be further data.

### Response Result Example

    //JSON
    {
       "Total":187,
       "Results":[
          {
             "id":"63591",
             "text":"Alexandra",
             "Tot":271
          }
       ]
    }

* * *

* * *

* * *

## 4\. Get ScheduleM

`Get The ScheduleM Data` [_get the ScheduleM data using the API_]

* * *

### Calling Parameters (Input)

<table>

<thead>

<tr>

<th style="text-align:left">Parameter</th>

<th style="text-align:left">Mode</th>

<th style="text-align:left">Description</th>

<th style="text-align:left">example values</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left">`suburb_id`</td>

<td style="text-align:left">int</td>

<td style="text-align:left">suburbs id</td>

<td style="text-align:left">63591</td>

</tr>

<tr>

<td style="text-align:left">`stage`</td>

<td style="text-align:left">int</td>

<td style="text-align:left">stage of loadshedding</td>

<td style="text-align:left">2</td>

</tr>

<tr>

<td style="text-align:left">`province_id`</td>

<td style="text-align:left">int</td>

<td style="text-align:left">provinces id</td>

<td style="text-align:left">9</td>

</tr>

<tr>

<td style="text-align:left">`municipality_total`</td>

<td style="text-align:left">int</td>

<td style="text-align:left">municipalitys total</td>

<td style="text-align:left">271</td>

</tr>

</tbody>

</table>

### Interface Address

https://loadshedding.eskom.co.za/LoadShedding/GetScheduleM/63591/2/9/271

### Example:

*   List load shedding schedule for suburb:
*   Call: http://loadshedding.eskom.co.za/LoadShedding/GetScheduleM/<_suburb_id_>/<_stage_>/<_province_id_>/<_municipality_total_>
*   municipality_total must be 1 or more.
    *   Example (Suburb = Hermanus, Stage = 2, Province = 9 (Western Cape)): http://loadshedding.eskom.co.za/LoadShedding/GetScheduleM/1061287/2/9/1
*   Returned HTML (you will need to parse).

### Request Method

*   HTTP
*   GET
*   POST

### Response Parameters (Output)

<table>

<thead>

<tr>

<th style="text-align:left">Parameter</th>

<th style="text-align:left">Mode</th>

<th style="text-align:left">Description</th>

<th style="text-align:left">example values</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left">`day`</td>

<td style="text-align:left">String</td>

<td style="text-align:left">day</td>

<td style="text-align:left">Wed, 09 Sep</td>

</tr>

<tr>

<td style="text-align:left">`time`</td>

<td style="text-align:left">String</td>

<td style="text-align:left">time</td>

<td style="text-align:left">06:00 - 08:30</td>

</tr>

</tbody>

</table>

### Response Result Example

    //html to parse
    Wed, 09 Sep
    06:00 - 08:30
    14:00 - 16:30
    Thu, 10 Sep
    14:00 - 16:30
    22:00 - 00:30
    Fri, 11 Sep
    22:00 - 00:30
    Sat, 12 Sep
    06:00 - 08:30
    Sun, 13 Sep
    04:00 - 06:30
    12:00 - 14:30
    Mon, 14 Sep
    12:00 - 14:30
    20:00 - 22:30
    Tue, 15 Sep
    20:00 - 22:30
    Wed, 16 Sep
    04:00 - 06:30
    Thu, 17 Sep
    02:00 - 04:30
    10:00 - 12:30
    Fri, 18 Sep
    10:00 - 12:30
    18:00 - 20:30
    Sat, 19 Sep
    18:00 - 20:30
    Sun, 20 Sep
    02:00 - 04:30
    Mon, 21 Sep
    00:00 - 02:30
    08:00 - 10:30
    Tue, 22 Sep
    08:00 - 10:30
    16:00 - 18:30
    Wed, 23 Sep
    16:00 - 18:30
    Thu, 24 Sep
    00:00 - 02:30
    Fri, 25 Sep
    06:00 - 08:30
    Sat, 26 Sep
    06:00 - 08:30
    14:00 - 16:30
    Sun, 27 Sep
    14:00 - 16:30
    22:00 - 00:30
    Mon, 28 Sep
    22:00 - 00:30
    Tue, 29 Sep
    04:00 - 06:30
    Wed, 30 Sep
    04:00 - 06:30
    12:00 - 14:30
    Thu, 01 Oct
    10:00 - 12:30
    18:00 - 20:30
    Fri, 02 Oct
    18:00 - 20:30
    Sat, 03 Oct
    02:00 - 04:30
    Sun, 04 Oct
    02:00 - 04:30
    10:00 - 12:30
    Mon, 05 Oct
    08:00 - 10:30
    16:00 - 18:30
    Tue, 06 Oct
    16:00 - 18:30
    Wed, 07 Oct
    00:00 - 02:30
    Find Print schedule

