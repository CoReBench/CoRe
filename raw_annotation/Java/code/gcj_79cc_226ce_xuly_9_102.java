import java.io.*;
import java.util.*;
public class Solution {
    private static Scanner in;
    public static double roundToDecimals(double value, int places) {
        double scale = Math.pow(10, places);
        return Math.round(value * scale) / scale;
    }
    public static void xuly(){
        double a = in.nextDouble();
        double[] centerX = {0.5,0,0};
        double[] centerY = {0,0.5,0};
        double[] centerZ = {0,0,0.5};
        double[] x0 = {0.5, 0.5, 0.5, 0.5,-0.5,-0.5,-0.5,-0.5};
        double[] y0 = {0.5, 0.5,-0.5,-0.5, 0.5, 0.5,-0.5,-0.5};
        double[] z0 = {0.5,-0.5,-0.5, 0.5,-0.5, 0.5,-0.5, 0.5};
        double i = 0;
        boolean isFound = false;
        while (i<=45){
            isFound = false;
            double rad = Math.toRadians(i);
            double[] xr = new double[8];
            double[] yr = new double[8];
            double[] zr = new double[8];
            for (int j = 0; j < 8; j++) {
                xr[j] = x0[j] * Math.cos(rad) - y0[j]* Math.sin(rad);
                yr[j] = x0[j] * Math.sin(rad) + y0[j]* Math.cos(rad);
                zr[j] = z0[j];
            }
            double x1 = 1,y1 = 1,x2 = -1,y2 = -1;
            for (int j = 0; j < 8; j++) {
                x1 = Math.min(x1,xr[j]);
                x2 = Math.max(x2,xr[j]);
                y1 = Math.min(y1,zr[j]);
                y2 = Math.max(y2,zr[j]);
            }
            double dt = (x2-x1) * (y2-y1) ;
            double diff = Math.abs(a - dt);
            double[] cX = new double[3];
            double[] cY = new double[3];
            double[] cZ = new double[3];
            for (int j = 0; j < 3; j++) {
                cX[j] = centerX[j] * Math.cos(rad) - centerY[j] * Math.sin(rad);
                cY[j] = centerX[j] * Math.sin(rad) + centerY[j] * Math.cos(rad);
                cZ[j] = centerZ[j];
            }
            if (diff <= 0.000001) {
                for (int j = 0; j < 3; j++) {
                    System.out.println(cX[j] + " " + cY[j] + " " + cZ[j]);
                }
                break;
            }
            else{
                double[] xr0 = new double[8];
                double[] yr0 = new double[8];
                double[] zr0 = new double[8];
                for (int j = 0; j < 8; j++) {
                    xr0[j] = xr[j];
                    yr0[j] = yr[j];
                    zr0[j] = zr[j];
                }
                double ii = 0;
                while (ii<=45) {
                    isFound = false;
                    double rad0 = Math.toRadians(ii);
                    for (int j = 0; j < 8; j++) {
                        xr[j] = xr0[j];
                        zr[j] = yr0[j] * Math.sin(rad0) + zr0[j] * Math.cos(rad0);
                    }
                    x1 = 1;
                    y1 = 1;
                    x2 = -1;
                    y2 = -1;
                    for (int j = 0; j < 8; j++) {
                        x1 = Math.min(x1, xr[j]);
                        x2 = Math.max(x2, xr[j]);
                        y1 = Math.min(y1, zr[j]);
                        y2 = Math.max(y2, zr[j]);
                    }
                    dt = (x2 - x1) * (y2 - y1);
                    diff = Math.abs(a - dt);
                    if (diff <= 0.000001) {
                        double[] cXn = new double[3];
                        double[] cYn = new double[3];
                        double[] cZn = new double[3];
                        for (int j = 0; j < 3; j++) {
                            cXn[j] = cX[j];
                            cYn[j] = cY[j] * Math.cos(rad0) - cZ[j] * Math.sin(rad0);
                            cZn[j] = cY[j] * Math.sin(rad0) + cZ[j] * Math.cos(rad0);
                            System.out.println(cXn[j] + " " + cYn[j] + " " + cZn[j]);
                        }
                        isFound = true;
                        break;
                    }
                    ii=roundToDecimals(ii+0.1,6);
                }
            }
            if (isFound) break;
            i=roundToDecimals(i+0.1,6);
        }
        System.out.flush();
    }
    public static void main(String[] args) throws IOException {
        in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int numCases = in.nextInt();
        for (int test = 1; test <= numCases; test++) {
            System.out.print("Case #" + test + ": ");
            xuly();
        }
    }
}