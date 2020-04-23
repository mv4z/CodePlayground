
import nhlstats.NHLStatistics;

public class Main {

    public static void main(String[] args) {
        System.out.println("Top 10 Players (Goals)\n");
        NHLStatistics.sortByGoals();
        NHLStatistics.top(10);
        
        System.out.println("Top 25 Players (Penalties)\n");
        NHLStatistics.sortByPenalties();
        NHLStatistics.top(25);
        
        System.out.println("Sidney Crosby Stats\n");
        NHLStatistics.searchByPlayer("Sidney Crosby");
        
        System.out.println("Philadelphia Flyers Stats\n");
        NHLStatistics.teamStatistics("PHI");
        
        System.out.println("Anaheim Ducks Roster\n");
        NHLStatistics.sortByPoints();
        NHLStatistics.teamStatistics("ANA");
    }
}
