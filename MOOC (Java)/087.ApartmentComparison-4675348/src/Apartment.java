
public class Apartment {

    private int rooms;
    private int squareMeters;
    private int pricePerSquareMeter;

    public Apartment(int rooms, int squareMeters, int pricePerSquareMeter) {
        this.rooms = rooms;
        this.squareMeters = squareMeters;
        this.pricePerSquareMeter = pricePerSquareMeter;
    }
    public boolean larger(Apartment otherApartment){
        return(this.squareMeters > otherApartment.squareMeters);
    }
    public int priceDifference(Apartment otherApartment){
        int diff = Math.abs(this.squareMeters * this.pricePerSquareMeter) - (otherApartment.squareMeters * otherApartment.pricePerSquareMeter);
        if(diff < 0){
            return Math.abs(diff);
        }
        return diff;
    }
    public boolean moreExpensiveThan(Apartment otherApartment){
        return this.pricePerSquareMeter > otherApartment.pricePerSquareMeter;
    }
}
