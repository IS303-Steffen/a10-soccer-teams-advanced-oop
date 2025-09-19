# Rubric
Your grade is based on whether you pass the automated tests, listed below.

The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.


<table border="1" style="width: 100%; text-align: center;">
<thead style="text-align: center;">
    <tr>
        <th style="text-align: center;">Test</th>
        <th style="text-align: center;">Description</th>
        <th style="text-align: center;">Points</th>
    </tr>
</thead>
<tbody>
    <tr style="text-align: left">
        <td>1. Input Prompts</td>
        <td>
        <b>Input test cases used:</b> 1-8<br><br>
        Your input prompts must be the same as the expected input prompts of each input test case. 
        <br>
        <br>
        See the <code>descriptions_ot_test_cases</code> folder for expected input prompts for each input test case.
        </td>
        <td>10</td>
    </tr>
    <tr style="text-align: left">
        <td>2. Printed Messages</td>
        <td>
        <b>Input test cases used:</b> 1-8<br><br>
        Your printed output must be the same as the expected output of each input test case.
        <br>
        <br>
        See the <code>descriptions_of_test_cases</code> folder for expected printed messages for each input test case.       
        </td> 
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td>3. SoccerTeam Class</td>
        <td style="text-align: left">
          This test will create SoccerTeam objects. The object should contain the instance variables listed in the top of this document.
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td>4. SponsoredTeam Class</td>
        <td style="text-align: left">
          This test will create SponsoredTeam objects. The object should contain the instance variables listed in the top of this document and inherit from SoccerTeam
        </td>
        <td>10</td>
    </tr>
      <tr>
        <td>5. Game Class</td>
        <td style="text-align: left">
          This test will create Game objects. The object should contain the instance variables listed in the top of this document.
        </td>
        <td>10</td>
    </tr>
          <tr>
        <td>6. SoccerTeam - record win</td>
        <td style="text-align: left">
          Will test that it correctly adds 1 to a SoccerTeam's wins variable
        </td>
        <td>3</td>
    </tr>
    <td>7. SoccerTeam - record loss</td>
        <td style="text-align: left">
          Will test that it correctly adds 1 to a SoccerTeam's losses variable
        </td>
        <td>3</td>
    </tr>
    <tr>
       <td>8. SoccerTeam - get record percentage</td>
        <td style="text-align: left">
          Will test that it returns a correctly calculated percentage rounded to the 2nd decimal.
        </td>
        <td>5</td>
    </tr>
        <tr>
       <td>9. SoccerTeam - generate score</td>
        <td style="text-align: left">
          Will test that it returns an integer between 0 and 3 inclusive.
        </td>
        <td>5</td>
    </tr>
    <tr>
       <td>10. SoccerTeam - get season message</td>
        <td style="text-align: left">
          Will test that it returns the correct message based on the season percentage
        </td>
        <td>5</td>
    </tr>
    <tr>
       <td>11. SponsoredTeam - generate score</td>
        <td style="text-align: left">
          Will test that it returns an integer between 1 and 3 inclusive
        </td>
        <td>5</td>
    </tr>
    <tr>
       <td>12. SponsoredTeam - get season message</td>
        <td style="text-align: left">
          Will test that it returns the correct message based on the season percentage (including the sponsor)
        </td>
        <td>5</td>
    </tr>
    <tr>
       <td>13. Game - play game</td>
        <td style="text-align: left">
          Ensures that all relevant instance variables in Game, SoccerTeam/SponsoredTeam are updated when playing a game.
        </td>
        <td>13</td>
    </tr>
    <tr>
       <td>14. No tie scores</td>
        <td style="text-align: left">
          Ensures that your code can't produce tie scores.
        </td>
        <td>5</td>
    </tr>
        <tr>
        <td>5. Sufficient Comments</td>
        <td style="text-align: left">Your code must include at least <code>15</code> comments. You can use any form of commenting:
        <ul>
          <li><code>#</code></li> 
          <li><code>''' '''</code></li>
          <li><code>""" """</code></li>
        </ul>
        </td>
        <td>1</td>
    </tr>
    <tr>
        <td colspan="2">Total Points</td>
        <td>100</td>
  </tr>
</tbody>
</table>

## Test Cases
If you fail a test during a specific test case, see the `descriptions_of_test_cases` folder for the following:
<table border="1" style="width: 100%; text-align: left;">
  <tr>
    <th>Test Case</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Input Test Case 01</td>
    <td>3 teams, 1 sponsored, 5 games, viewing multiple teams and games</td>
  </tr>
  <tr>
    <td>Input Test Case 02</td>
    <td>3 teams, 1 sponsored, 5 games, but with different capitalization, leading and trailing spaces</td>
  </tr>
  <tr>
    <td>Input Test Case 03</td>
    <td>3 teams, 1 sponsored team, but no games played to test handling of potential zero division error</td>
  </tr>
  <tr>
    <td>Input Test Case 04</td>
    <td>Invalid integer and values less than 2 for the number of teams to create</td>
  </tr>
  <tr>
    <td>Input Test Case 05</td>
    <td>Invalid inputs for teams and putting the same number for the home and away teams.</td>
  </tr>
  <tr>
    <td>Input Test Case 06</td>
    <td>Invalid Postseason menu option</td>
  </tr>
  <tr>
    <td>Input Test Case 07</td>
    <td>Invalid Team Info Menu option</td>
  </tr>
  <tr>
    <td>Input Test Case 08</td>
    <td>Invalid Game Info Menu option</td>
  </tr>
</table>
